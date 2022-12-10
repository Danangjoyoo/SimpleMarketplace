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


def insert_image(image_url: str):
    """
    insert into image (image_url) values (<image_url>)
    """
    image = Image(url=image_url)
    session.add(image)
    handle_commit()

    return image


def update_image(image_id: int, image_url: str):
    """
    update image p
    set p.name = name, p.description = description
    where p.id = image_id
    """
    image = select_specific_image(image_id)

    if not image:
        raise InvalidProcess("image not found", 400)

    image.url = image_url

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


def select_specific_image_collection(image_collection_id: int) -> Image:
    """
    select * from image p where p.id = image_id
    """
    image = session.query(
        Image_Collection
    ).filter(
        Image_Collection.id == image_collection_id
    ).first()

    return image


def insert_image_collection():
    """
    insert into image (name, description) values (<name>, <description>)
    """
    image = Image_Collection()
    session.add(image)
    handle_commit()

    return image


def delete_from_image_collection(image_collection_id: int):
    """
    delete from image
    where image.id = image_id
    """
    image = select_specific_image_collection(image_collection_id)

    if not image:
        raise InvalidProcess("image not found", 400)

    session.delete(image)

    handle_commit()


def register_image_collection(image_collection_id: int, image_id: int):
    """
    """
    new_collection_link = Image_Collection_Link(
        image_collection_id=image_collection_id,
        image_id=image_id
    )
    session.add(new_collection_link)
    handle_commit()
