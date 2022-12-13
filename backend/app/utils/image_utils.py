"""
Image utils
"""
import os
import requests
from werkzeug.datastructures import FileStorage

from app.utils.exception import InvalidProcess


def process_image_upload(image_file: FileStorage):
    """
    process image upload to data storage
    """
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
