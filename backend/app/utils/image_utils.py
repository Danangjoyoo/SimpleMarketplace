"""
Image utils
"""
from app.utils.exception import InvalidProcess

def verify_image(image):
    return


def upload_image_to_storage(image):
    return


def process_image_upload(image):
    if not verify_image(image):
        raise InvalidProcess("invalid image")

    upload_image_to_storage(image)