"""
Product Logic Controllers
"""
from chain_logging.flask import logger
from uuid import uuid4

from app.queries import as_dict
from app.queries.image_query import (
    select_product_image_list, insert_image, insert_image_collection,
    select_variant_image_list_from_product, select_highlight_image_product
)
from app.queries.product_query import (
    select_product_list, select_specific_product_details, insert_product,
    update_product, delete_from_product
)
from app.queries.variant_query import (
    select_variant_list
)
from app.utils.exception import InvalidProcess


def get_product_list(page: int, row: int):
    """
    """
    try:
        logger.info(f"get product list {page=} {row=}")

        product_list = select_product_list(page, row)
        product_list = as_dict(product_list)

        if product_list:
            highlight_image_list = select_highlight_image_product([prod["product_id"] for prod in product_list])
            highlight_image_map = {
                image.product_id: image.image_url
                for image in highlight_image_list
            }

            for product in product_list:
                product["highligt_image_url"] = highlight_image_map.get(product["product_id"])

        return product_list

    except Exception as error:
        logger.error(f"failed to get product list : {error}")
        InvalidProcess.handle_exception(error)


def get_specific_product(product_id: int):
    """
    """
    try:
        logger.info(f"get specific product {product_id=}")

        product = select_specific_product_details(product_id)
        product = as_dict(product)

        images = select_product_image_list(product_id)
        images = as_dict(images)

        if product:
            product["images"] = images

            variant_list = select_variant_list(product_id)
            variant_list = as_dict(variant_list)

            variant_image_list = select_variant_image_list_from_product(product_id)
            variant_image_map = {}

            for var in variant_image_list:
                if var.variant_id not in variant_image_map:
                    variant_image_map[var.variant_id] = []

                variant_image_map[var.variant_id].append({
                    "image_id": var.image_id,
                    "image_url": var.image_url
                })

            for var in variant_list:
                var["images"] = variant_image_map.get(var["id"], [])

            product["variant_list"] = variant_list

        return product

    except Exception as error:
        logger.error(f"failed to get specific product : {error}")
        InvalidProcess.handle_exception(error)


def post_product(name: str, description: str):
    """
    """
    try:
        logger.info(f"create product {name=}")

        # preserve collection
        image_collection = insert_image_collection()

        # preserve logo
        image_logo = insert_image()

        # create product
        product = insert_product(name, description, image_collection.id, image_logo.id)
        product = as_dict(product)

        logger.info(f"product created {product=}")

        return product

    except Exception as error:
        logger.error(f"failed to get specific product : {error}")
        InvalidProcess.handle_exception(error)


def put_product(product_id: int, name: str, description: str):
    """
    """
    try:
        logger.info(f"update product {product_id=}")

        product = update_product(product_id, name, description)
        product = as_dict(product)

        logger.info(f"product updated {product_id=}")

        return product

    except Exception as error:
        logger.error(f"failed to update product : {error}")
        InvalidProcess.handle_exception(error)


def delete_product(product_id: int):
    """
    """
    try:
        logger.info(f"delete product {product_id=}")

        delete_from_product(product_id)
        status = {"status": 1}

        logger.info(f"product deleted {product_id=}")

        return status

    except Exception as error:
        logger.error(f"failed to update product : {error}")
        InvalidProcess.handle_exception(error)
