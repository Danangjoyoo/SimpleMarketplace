"""
Variant Query File
"""
from typing import List

from app.database.connection import session
from app.database.models import Variant
from app.utils.exception import handle_commit, InvalidProcess


def select_variant_list(product_id: int, page: int, row: int) -> List[Variant]:
    """
    select * from variant
    """
    variant_list = session.query(
        Variant
    ).filter(
        Variant.product_id == product_id
    ).offset(
        (page - 1) * row
    ).limit(row).all()

    return variant_list


def select_specific_variant(variant_id: int) -> Variant:
    """
    select * from variant p where p.id = variant_id
    """
    variant = session.query(
        Variant
    ).filter(
        Variant.id == variant_id
    ).first()

    return variant


def insert_variant(product_id: int, name: str, size: str, color: str):
    """
    insert into variant (name, description) values (<name>, <description>)
    """
    variant = Variant(
        product_id=product_id,
        name=name,
        size=size,
        color=color
    )

    session.add(variant)
    handle_commit()

    return variant


def update_variant(variant_id: int, name: str, size: str, color: str):
    """
    update variant p
    set p.name = name, p.description = description
    where p.id = variant_id
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
    delete from variant
    where variant.id = variant_id
    """
    variant = select_specific_variant(variant_id)

    if not variant:
        raise InvalidProcess("variant not found", 400)

    session.delete(variant)

    handle_commit()
