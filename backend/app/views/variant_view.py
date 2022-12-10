"""
Variant Views
"""
from chain_logging.flask import logger
from flask_toolkits import Path, Header, Query, Body, File
from flask_toolkits.responses import JSONResponse

from app.controllers import variant_controller as controller


def get_variant_list_view(
    product_id: int = Path(),
    page: int = Query(1),
    row: int = Query(10)
):
    result = controller.get_variant_list(product_id, page, row)
    return JSONResponse(result)


def get_variant_view(
    variant_id: int = Query()
):
    result = controller.get_specific_variant(variant_id)
    return JSONResponse(result)


def create_variant_view(
    name: str = Body(),
    description: str = Body()
):
    result = controller.post_variant(name, description)
    return JSONResponse(result)


def update_variant_view(
    variant_id: int = Path(),
    name: str = Body(),
    description: str = Body()
):
    result = controller.put_variant(variant_id, name, description)
    return JSONResponse(result)


def delete_variant_view(
    variant_id: int = Path()
):
    result = controller.delete_variant(variant_id)
    return JSONResponse(result)
