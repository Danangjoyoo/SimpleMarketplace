"""
Variant Logic Controllers
"""
from chain_logging.flask import logger

from app.queries import as_dict
from app.queries.image_query import insert_image_collection, select_variant_image_collection
from app.queries.variant_query import (
    select_variant_list, select_specific_variant, insert_variant,
    update_variant, delete_from_variant
)
from app.utils.exception import InvalidProcess



def get_variant_list(product_id: int):
    """
    """
    try:
        logger.info(f"get variant list {product_id=}")

        variant_list = select_variant_list(product_id)
        variant_list = as_dict(variant_list)

        return variant_list

    except Exception as error:
        logger.error(f"failed to get variant list : {error}")
        InvalidProcess.handle_exception(error)


def get_specific_variant(variant_id: int):
    """
    """
    try:
        logger.info(f"get specific variant {variant_id=}")

        variant = select_specific_variant(variant_id)
        variant = as_dict(variant)

        if variant:
            image_list = select_variant_image_collection(variant_id)
            variant["images"] = as_dict(image_list)

        return variant

    except Exception as error:
        logger.error(f"failed to get specific variant : {error}")
        InvalidProcess.handle_exception(error)


def post_variant(product_id: int, name: str, size: str, color: str):
    """
    """
    try:
        logger.info(f"create variant {name=}")

        image_collection = insert_image_collection()
        variant = insert_variant(product_id, image_collection.id, name, size, color)
        variant = as_dict(variant)

        logger.info(f"variant created {variant=}")

        return variant

    except Exception as error:
        logger.error(f"failed to get specific variant : {error}")
        InvalidProcess.handle_exception(error)


def put_variant(variant_id: int, name: str, size: str, color: str):
    """
    """
    try:
        logger.info(f"update variant {variant_id=}")

        variant = update_variant(variant_id, name, size, color)
        variant = as_dict(variant)

        logger.info(f"variant updated {variant_id=}")

        return variant

    except Exception as error:
        logger.error(f"failed to update variant : {error}")
        InvalidProcess.handle_exception(error)


def delete_variant(variant_id: int):
    """
    """
    try:
        logger.info(f"delete variant {variant_id=}")

        delete_from_variant(variant_id)
        status = {"status": 1}

        logger.info(f"variant deleted {variant_id=}")

        return status

    except Exception as error:
        logger.error(f"failed to update variant : {error}")
        InvalidProcess.handle_exception(error)
