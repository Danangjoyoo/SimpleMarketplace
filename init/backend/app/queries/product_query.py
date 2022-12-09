"""
Product Query File
"""
from typing import List

from app.database.connection import session
from app.database.models import Product
from app.utils.exception import handle_commit, InvalidProcess


def select_product_list(page: int, row: int) -> List[Product]:
    """
    select * from product
    """
    product_list = session.query(
        Product
    ).offset(
        (page - 1) * row
    ).limit(row).all()

    return product_list


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


def insert_product(name: str, description: str):
    """
    insert into product (name, description) values (<name>, <description>)
    """
    product = Product(name=name, description=description)
    session.add(product)
    handle_commit(error_message="failed to create product")

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

    handle_commit("failed to update product info")

    return product
