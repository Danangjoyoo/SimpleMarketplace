"""
Product Logic Controllers
"""
from chain_logging.flask import logger
from flask_toolkits.responses import JSONResponse

from app.queries import as_dict
from app.queries.product_query import (
    select_product_list, select_specific_product, insert_product
)
from app.utils.exception import InvalidProcess


def get_product_list(page: int, row: int):
    """
    """
    try:
        logger.info(f"get product list {row=} {page=}")

        product_list = select_product_list(page, row)
        product_list = as_dict(product_list)

        return product_list

    except Exception as error:
        logger.error(f"failed to get product list : {error}")
        InvalidProcess.handle_exception(error)


def get_specific_product(product_id: int):
    """
    """
    try:
        logger.info(f"get specific product {product_id=}")

        product = select_specific_product(product_id)
        product = as_dict(product)

        return product

    except Exception as error:
        logger.error(f"failed to get specific product : {error}")
        InvalidProcess.handle_exception(error)


def post_product(name: str, description: str):
    """
    """
    try:
        logger.info(f"create product {name=}")

        product = insert_product(name, description)
        product = as_dict(product)

        return product

    except Exception as error:
        logger.error(f"failed to get specific product : {error}")
        InvalidProcess.handle_exception(error)


def post_product(product_id: int, name: str, description: str):
    """
    """
    try:
        logger.info(f"create product {name=}")

        product = insert_product(name, description)
        product = as_dict(product)

        return product

    except Exception as error:
        logger.error(f"failed to get specific product : {error}")
        InvalidProcess.handle_exception(error)
