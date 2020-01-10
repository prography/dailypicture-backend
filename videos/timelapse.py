from django.conf import settings
from django.core.files.storage import default_storage
import os
import shutil
import cv2
import boto3
from PIL import Image


class Timelapse:
    image_base_path = "./temp_image"
    timelapse_base_path = "./temp_timelapse"
    fps = 30
    imageps = 5
    try:
        s3 = True
        s3client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
    except AttributeError:
        s3 = False

    def __init__(self, image_urls, title, post_id):
        self.image_urls = image_urls
        self.title = title
        self.image_path = os.path.join(self.image_base_path, post_id)
        self.post_id = post_id
        self.timelapse_path = os.path.join(self.timelapse_base_path, post_id)

        if not os.path.isdir(self.image_path):
            os.makedirs(self.image_path)
        if not os.path.isdir(self.timelapse_path):
            os.makedirs(self.timelapse_path)

        if self.s3:
            self.saveFromS3()
        else:
            upload_path = os.path.join(settings.MEDIA_ROOT, "video", post_id)
            if not os.path.isdir(upload_path):
                os.makedirs(upload_path)
            self.saveFromLocal()

    # 저장소에서 서버로 이미지들을 다운로드
    def saveFromS3(self):
        self.image_list = []
        for image in self.image_urls:
            image_base_path = os.path.join(self.image_path, image.name.split("/")[-1])
            self.image_list.append(image_base_path)
            self.s3client.download_file(
                settings.AWS_STORAGE_BUCKET_NAME, "media/" + image.name, image_base_path
            )

    def saveFromLocal(self):
        self.image_list = []
        for image in self.image_urls:
            image_base_path = os.path.join(self.image_path, image.name.split("/")[-1])
            self.image_list.append(image_base_path)
            image_path = image.path
            shutil.copy2(image_path, self.image_path)

    # 변환 후 임시로 저장한 이미지 삭제
    def delete(self):
        if os.path.isdir(self.image_path):
            shutil.rmtree(self.image_path)
        if os.path.isdir(self.timelapse_path):
            shutil.rmtree(self.timelapse_path)

    # 영상, animated-gif 변환
    def make(self, file_ext):
        if file_ext == "mp4":
            timelapse = self.makeVideo()
        elif file_ext == "gif":
            timelapse = self.makeGif()
        upload_file_name = "video/" + self.post_id + "/" + self.title + "." + file_ext

        if self.s3:
            self.saveToS3(upload_file_name, timelapse)
        else:
            self.saveToLocal(upload_file_name, timelapse)

        self.timelapse_url = default_storage.url(name=upload_file_name)
        self.delete()
        return self.timelapse_url

    # 영상 변환
    def makeVideo(self):
        images = [cv2.imread(image) for image in self.image_list]
        height, width, channel = images[0].shape
        timelapse = os.path.join(self.timelapse_path, self.title + ".mp4")
        writer = cv2.VideoWriter(
            timelapse, cv2.VideoWriter_fourcc(*"mp4v"), self.fps, (width, height)
        )

        for frame in images:
            for _ in range(self.fps // self.imageps):
                writer.write(frame)
        writer.release()
        return timelapse

    # animated-gif 변환
    def makeGif(self):
        images = [Image.open(image) for image in self.image_list]
        timelapse = os.path.join(self.timelapse_path, self.title + ".gif")
        images[0].save(
            timelapse,
            save_all=True,
            append_images=images[1:],
            duration=int(1 / self.imageps * 1000),
            loop=0,
        )
        return timelapse

    # MEDIA_ROOT에 영상 저장
    def saveToLocal(self, upload_file_name, timelapse):
        with open(timelapse, "rb") as timelapse_byte:
            with default_storage.open(upload_file_name, "wb") as save_file:
                save_file.write(timelapse_byte.read())

    def saveToS3(self, upload_file_name, timelapse):
        upload_file_path = "media/" + upload_file_name
        self.s3client.upload_file(
            timelapse,
            settings.AWS_STORAGE_BUCKET_NAME,
            upload_file_path,
            ExtraArgs={"ACL": "public-read"},
        )
