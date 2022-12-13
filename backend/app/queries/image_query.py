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
    get the first image uploaded in collection as a highlight
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
    list and paginate all of product images
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
    get variant list of a product
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


def select_variant_image_collection(variant_id: int):
    """
    get variant image collection
    """
    highlight_image_list = session.query(
        Variant.id.label("variant_id"),
        Image.url.label("image_url")
    ).join(
        Image_Collection,
        Image_Collection.id == Variant.images
    ).join(
        Image_Collection_Link,
        Image_Collection_Link.image_collection_id == Image_Collection.id
    ).join(
        Image,
        Image.id == Image_Collection_Link.image_id
    ).filter(
        Variant.id == variant_id
    ).all()

    return highlight_image_list


def select_highlight_image_variant(variant_id_list: List[int]):
    """
    get the first image uploaded in collection as a highlight
    """
    highlight_image_list = session.query(
        Variant.id.label("variant_id"),
        Image.url.label("image_url")
    ).join(
        Image_Collection,
        Image_Collection.id == Variant.images
    ).outerjoin(
        Image_Collection_Link,
        Image_Collection_Link.image_collection_id == Image_Collection.id
    ).outerjoin(
        Image,
        Image.id == Image_Collection_Link.image_id
    ).filter(
        Variant.id.in_(variant_id_list)
    ).group_by(
        Variant.id
    ).all()

    return highlight_image_list


def insert_image(image_url: Optional[str] = None):
    """
    add row to image table
    """
    image = Image(url=image_url)
    session.add(image)
    handle_commit()

    return image


def update_image(image_id: int, image_url: str):
    """
    update specific row of image table
    """
    image = select_specific_image(image_id)

    if not image:
        raise InvalidProcess("image not found", 400)

    image.url = image_url

    handle_commit()

    return image


def delete_from_image(image_id: int):
    """
    delete specific row from image table
    """
    image = select_specific_image(image_id)

    if not image:
        raise InvalidProcess("image not found", 400)

    session.delete(image)

    handle_commit()


def insert_image_collection():
    """
    add new image collection row
    """
    image = Image_Collection()
    session.add(image)
    handle_commit()

    return image


def register_image_collection(image_collection_id: int, image_id: int):
    """
    add a link between image and image collection table
    """
    new_collection_link = Image_Collection_Link(
        image_collection_id=image_collection_id,
        image_id=image_id
    )
    session.add(new_collection_link)
    handle_commit()
