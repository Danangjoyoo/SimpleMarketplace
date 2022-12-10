"""
Image Query File
"""
from typing import List

from app.database.connection import session
from app.database.models import Image, Image_Collection, Image_Collection_Link
from app.utils.exception import handle_commit, InvalidProcess


def select_image_list(page: int, row: int) -> List[Image]:
    """
    select * from image
    """
    image_list = session.query(
        Image
    ).offset(
        (page - 1) * row
    ).limit(row).all()

    return image_list


def select_specific_image(image_id: int) -> Image:
    """
    select * from image p where p.id = image_id
    """
    image = session.query(
        Image
    ).filter(
        Image.id == image_id
    ).first()

    return image


def insert_image(name: str, description: str):
    """
    insert into image (name, description) values (<name>, <description>)
    """
    image = Image(name=name, description=description)
    session.add(image)
    handle_commit()

    return image


def update_image(image_id: int, name: str, description: str):
    """
    update image p
    set p.name = name, p.description = description
    where p.id = image_id
    """
    image = select_specific_image(image_id)

    if not image:
        raise InvalidProcess("image not found", 400)

    image.name = name
    image.description = description

    handle_commit()

    return image


def delete_from_image(image_id: int):
    """
    delete from image
    where image.id = image_id
    """
    image = select_specific_image(image_id)

    if not image:
        raise InvalidProcess("image not found", 400)

    session.delete(image)

    handle_commit()
