"""
Variant Views
"""
from flask_toolkits import Path, Header, Query, Body, File
from flask_toolkits.responses import JSONResponse
from typing import Optional

from app.controllers import variant_controller as controller


def get_variant_list_view(
    product_id: int = Path()
):
    result = controller.get_variant_list(product_id)
    return JSONResponse(result)


def get_variant_view(
    variant_id: int = Query()
):
    result = controller.get_specific_variant(variant_id)
    return JSONResponse(result)


def create_variant_view(
    product_id: int = Path(),
    name: Optional[str] = Body(None),
    size: Optional[str] = Body(None),
    color: Optional[str] = Body(None)
):
    result = controller.post_variant(product_id, name, size, color)
    return JSONResponse(result)


def update_variant_view(
    variant_id: int = Path(),
    name: Optional[str] = Body(None),
    size: Optional[str] = Body(None),
    color: Optional[str] = Body(None)
):
    result = controller.put_variant(variant_id, name, size, color)
    return JSONResponse(result)


def delete_variant_view(
    variant_id: int = Path()
):
    result = controller.delete_variant(variant_id)
    return JSONResponse(result)
