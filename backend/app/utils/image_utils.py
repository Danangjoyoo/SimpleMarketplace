"""
Image utils
"""
import os
import requests
from chain_logging.flask import logger
from PIL import Image
from werkzeug.datastructures import FileStorage

from app.utils.exception import InvalidProcess


def verify_image(image_file: FileStorage):
    try:
        pil_image = Image.open(image_file)
        pil_image.verify()
        return pil_image
    except Exception as error:
        logger.error(f"image verification failed : {error}")
        raise InvalidProcess(f"invalid image : {error}")


def upload_image_to_storage(image_file: FileStorage):
    # upload to storage
    upload_url = os.getenv("STORAGE_URL")+"/add"
    response = requests.post(
        url=upload_url,
        files={
            "file": (
                image_file.filename,
                image_file.stream,
                image_file.content_type,
                image_file.headers
            )
        }
    )

    if response.status_code != 200:
        raise InvalidProcess("image upload failed", 500)

    return response.json().get("url")


def process_image_upload(image_file: FileStorage):
    # verify_image(image_file)

    return upload_image_to_storage(image_file)