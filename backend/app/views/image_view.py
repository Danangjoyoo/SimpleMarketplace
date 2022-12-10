"""
Image Views
"""
from flask import jsonify
from flask_toolkits import Path, Header, Query, Body, File, Form
from flask_toolkits.responses import JSONResponse
from typing import Optional
from werkzeug.datastructures import FileStorage

from app.controllers import image_controller as controller
from app.schema.image_schema import ImageEntityEnum


def create_image_view(
    entity_type: ImageEntityEnum = Form(),
    image: FileStorage = File()
):
    result = controller.post_image()
    return JSONResponse(result)

def delete_image_view(image_id: int = Path()):
    return
