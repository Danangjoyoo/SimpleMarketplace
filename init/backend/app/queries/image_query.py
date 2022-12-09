"""
Image Query File
"""
from app.database.connection import session
from app.database.models import Image, Image_Collection, Image_Collection_Link


def select_image_by_id(image_id: int):
    pass