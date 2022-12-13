"""
Product Query File
"""
from typing import List

from app.database.connection import session
from app.database.models import Image, Image_Collection, Image_Collection_Link, Product, Variant
from app.utils.exception import handle_commit, InvalidProcess


def select_product_name_by_keyword(keyword: str):
    """
    """
    product_list = session.query(
        Product.id,
        Product.name
    ).filter(
        Product.name.like(f"%{keyword}%")
    ).limit(5).all()

    return product_list


def select_product_list(page: int, row: int) -> List[Product]:
    """
    select * from product
    """
    product_list = session.query(
        Product.id.label("product_id"),
        Product.name.label("product_name"),
        Image.url.label("logo_url")
    ).join(
        Image,
        Image.id == Product.logo_id
    ).offset(
        (page - 1) * row
    ).limit(row).all()

    return product_list


def select_specific_product_details(product_id: int):
    product = session.query(
        Product.name,
        Product.description,
        Product.created_at,
        Image.url.label("logo_url")
    ).join(
        Image,
        Image.id == Product.logo_id
    ).filter(
        Product.id == product_id
    ).first()

    return product


def select_specific_product(product_id: int) -> Product:
    """
    select * from product p where p.id = product_id
    """
    product = session.query(
        Product
    ).filter(
        Product.id == product_id
    ).first()

    return product


def insert_product(name: str, description: str, image_collection_id: int, logo_id: int):
    """
    insert into product (name, description) values (<name>, <description>)
    """
    product = Product(name=name, description=description, images=image_collection_id, logo_id=logo_id)
    session.add(product)
    handle_commit()

    return product


def update_product(product_id: int, name: str, description: str):
    """
    update product p
    set p.name = name, p.description = description
    where p.id = product_id
    """
    product = select_specific_product(product_id)

    if not product:
        raise InvalidProcess("product not found", 400)

    product.name = name
    product.description = description

    handle_commit()

    return product


def delete_from_product(product_id: int):
    """
    delete from product
    where product.id = product_id
    """
    product = select_specific_product(product_id)

    if not product:
        raise InvalidProcess("product not found", 400)

    session.delete(product)

    handle_commit()
