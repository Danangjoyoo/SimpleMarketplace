"""
Image utils
"""
import os
import requests
from PIL import Image
from werkzeug.datastructures import FileStorage

from app.utils.exception import InvalidProcess

def verify_image(image_file: FileStorage):
    pil_image = Image.open(image_file)
    pil_image.verify()


def upload_image_to_storage(image_file: FileStorage):
    upload_url = os.getenv("STORAGE_URL")+"/add"
    response = requests.post(upload_url, {"file": image_file.stream})

    if response.status_code != 200:
        raise InvalidProcess("image upload failed", 500)

    return response.json().get("url")


def process_image_upload(image_file: FileStorage):
    if not verify_image(image_file):
        raise InvalidProcess("invalid image")

    return upload_image_to_storage(image_file)