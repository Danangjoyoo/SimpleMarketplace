"""
Variant Query File
"""
from typing import List

from app.database.connection import session
from app.database.models import Variant
from app.utils.exception import handle_commit, InvalidProcess


def select_variant_list(product_id: int) -> List[Variant]:
    """
    get all variant of a product
    """
    variant_list = session.query(
        Variant
    ).filter(
        Variant.product_id == product_id
    ).all()

    return variant_list


def select_specific_variant(variant_id: int) -> Variant:
    """
    get specific variant
    """
    variant = session.query(
        Variant
    ).filter(
        Variant.id == variant_id
    ).first()

    return variant


def insert_variant(
    product_id: int,
    image_collection_id: int,
    name: str,
    size: str,
    color: str
):
    """
    insert new row to variant table
    """
    variant = Variant(
        product_id=product_id,
        images=image_collection_id,
        name=name,
        size=size,
        color=color
    )

    session.add(variant)
    handle_commit()

    return variant


def update_variant(variant_id: int, name: str, size: str, color: str):
    """
    update specific row from variant table
    """
    variant = select_specific_variant(variant_id)

    if not variant:
        raise InvalidProcess("variant not found", 400)

    variant.name = name
    variant.size = size
    variant.color = color

    handle_commit()

    return variant


def delete_from_variant(variant_id: int):
    """
    delete specific row from variant table
    """
    variant = select_specific_variant(variant_id)

    if not variant:
        raise InvalidProcess("variant not found", 400)

    session.delete(variant)

    handle_commit()
