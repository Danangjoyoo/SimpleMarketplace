"""
Product Views
"""
from chain_logging.flask import logger
from flask_toolkits import Path, Header, Query, Body, File
from flask_toolkits.responses import JSONResponse

from app.controllers.product_controller import (
    get_product_list, get_specific_product, post_product,
    put_product, delete_product
)

def get_product_list_view(
    page: int = Query(1),
    row: int = Query(10)
):
    result = get_product_list(page, row)
    return JSONResponse(result)


def get_product_view(
    product_id: int = Query()
):
    result = get_specific_product(product_id)
    return JSONResponse(result)


def create_product_view(
    name: str = Body(),
    description: str = Body()
):
    result = post_product(name, description)
    return JSONResponse(result)


def update_product_view(
    product_id: int = Path(),
    name: str = Body(),
    description: str = Body()
):
    result = put_product(product_id, name, description)
    return JSONResponse(result)


def delete_product_view(
    product_id: int = Path()
):
    result = delete_product(product_id)
    return JSONResponse(result)
