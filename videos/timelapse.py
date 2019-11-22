from django.conf import settings
from django.core.files.storage import default_storage
import os
import shutil
import cv2
import boto3

class Timelapse:
    temp_image_path = "./temp_image"
    video_base_path = "./temp_video"
    fps = 60
    imageps = 5
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )

    def __init__(self, image_urls, title, post_id):
        self.image_urls = image_urls
        self.title = title
        self.image_path = os.path.join(self.temp_image_path, str(post_id))
        self.post_id = post_id
        self.video_path = os.path.join(self.video_base_path,
                                       str(post_id))
        if not os.path.isdir(self.temp_image_path):
            os.mkdir(self.temp_image_path)
        if not os.path.isdir(self.image_path):
            os.mkdir(self.image_path)
        if not os.path.isdir(self.video_base_path):
            os.mkdir(self.video_base_path)
        if not os.path.isdir(self.video_path):
            os.mkdir(self.video_path)
        self.save()

    # 저장소에서 서버로 이미지들을 다운로드
    def save(self):
        self.image_list = []
        for url in self.image_urls:
            image_name = os.path.join(self.image_path, url.split('/')[-1])
            self.image_list.append(image_name)
            self.s3.download_file(settings.AWS_STORAGE_BUCKET_NAME,
                                  'media/' + url, image_name)
            
    # 변환 후 임시로 저장한 이미지 삭제
    def delete(self):
        if os.path.isdir(self.image_path):
            shutil.rmtree(self.image_path)

    # 비디오 변환
    def make(self):
        images = [cv2.imread(image) for image in self.image_list]
        height, width, channel = images[0].shape
        video = os.path.join(self.video_path, self.title + ".mp4")
        writer = cv2.VideoWriter(video,
                                 cv2.VideoWriter_fourcc(*"mp4v"),
                                 self.fps,
                                 (width, height))

        for frame in images:
            for _ in range(self.fps//self.imageps):
                writer.write(frame)
        writer.release()
        
        upload_file_name = 'video/' + str(self.post_id) + '/' + self.title + ".mp4"
        upload_file_path = 'media/' + upload_file_name
        self.s3.upload_file(video, settings.AWS_STORAGE_BUCKET_NAME,
                            upload_file_path, ExtraArgs={'ACL':'public-read'})

        self.video_url = default_storage.url(name=upload_file_name)
        print(self.video_url)
        self.delete()
        return self.video_url