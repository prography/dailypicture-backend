from django.conf import settings
import os
import shutil
import cv2


class Timelapse:
    temp_image_path = "./temp_image"
    video_base_path = os.path.join(settings.MEDIA_ROOT, "video")
    fps = 60
    imageps = 5

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

    # 저장소에서 서버로 이미지들을 다운로드
    def save(self):
        for image in self.image_urls:
            image_url = './media/' + image
            print(image_url, self.image_path)
            shutil.copy2(image_url, self.image_path)

    # 변환 후 임시로 저장한 이미지 삭제
    def delete(self):
        if os.path.isdir(self.image_path):
            shutil.rmtree(self.image_path)

    # 비디오 변환
    def make(self):
        images = [cv2.imread(os.path.join(self.image_path, image))
                  for image in os.listdir(self.image_path)]
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
        self.video_url = "http://localhost:8000/media/video/" + \
            str(self.post_id) + '/' + self.title + ".mp4"

        self.delete()
        return self.video_url
