"""
Image Query File
"""
from typing import List, Optional

from app.database.connection import session
from app.database.models import Image, Image_Collection, Image_Collection_Link, Product, Variant
from app.utils.exception import handle_commit, InvalidProcess


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


def select_highlight_image_product(product_id_list: List[int]):
    """
    """
    highlight_image_list = session.query(
        Product.id.label("product_id"),
        Image.url.label("image_url")
    ).join(
        Image_Collection,
        Image_Collection.id == Product.images
    ).outerjoin(
        Image_Collection_Link,
        Image_Collection_Link.image_collection_id == Image_Collection.id
    ).outerjoin(
        Image,
        Image.id == Image_Collection_Link.image_id
    ).filter(
        Product.id.in_(product_id_list)
    ).group_by(
        Product.id
    ).all()

    return highlight_image_list


def select_product_image_list(
    product_id: int,
    page: int = None,
    row: int = 5
) -> List[Image]:
    """
    select * from image_collection_list icl
    """
    product_image_query = session.query(
        Image
    ).join(
        Image_Collection_Link,
        Image_Collection_Link.image_id == Image.id
    ).join(
        Image_Collection,
        Image_Collection.id == Image_Collection_Link.image_collection_id
    ).join(
        Product,
        Product.images == Image_Collection.id
    ).filter(
        Product.id == product_id
    )

    # to avoid 0 and None, use `is not`
    if page is not None:
        product_image_query = product_image_query.offset((page - 1) * row).limit(row)

    product_image_list = product_image_query.all()

    return product_image_list


def select_variant_image_list_from_product(product_id: int):
    """
    """
    product_variant_image_list = session.query(
        Variant.id.label("variant_id"),
        Image.id.label("image_id"),
        Image.url.label("image_url")
    ).join(
        Image_Collection_Link,
        Image_Collection_Link.image_id == Image.id
    ).join(
        Image_Collection,
        Image_Collection.id == Image_Collection_Link.image_collection_id
    ).join(
        Variant,
        Variant.images == Image_Collection.id
    ).join(
        Product,
        Product.id == Variant.product_id
    ).filter(
        Product.id == product_id
    ).all()

    return product_variant_image_list




def insert_image(image_url: Optional[str] = None):
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
