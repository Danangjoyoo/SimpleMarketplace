"""
Image Views
"""
from flask_toolkits import Path, File
from flask_toolkits.responses import JSONResponse
from werkzeug.datastructures import FileStorage

from app.controllers import image_controller as controller


def update_product_logo_view(
    product_id: int = Path(),
    image_file: FileStorage = File(),
):
    result = controller.put_product_logo(product_id, image_file)
    return JSONResponse(result)


def add_product_image_collection_view(
    product_id: int = Path(),
    image_file: FileStorage = File()
):
    result = controller.post_product_image_collection(product_id, image_file)
    return JSONResponse(result)


def add_variant_image_collection_view(
    variant_id: int = Path(),
    image_file: FileStorage = File()
):
    result = controller.post_variant_image_collection(variant_id, image_file)
    return JSONResponse(result)


def delete_image_view(
    image_id: int = Path()
):
    result = controller.delete_image(image_id)
    return JSONResponse(result)
