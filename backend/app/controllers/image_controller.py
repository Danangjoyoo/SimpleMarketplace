"""
Image Logic Controllers
"""
from werkzeug.datastructures import FileStorage

from app.schema.image_schema import ImageEntityEnum
from app.utils import image_utils
from app.utils.exception import InvalidProcess


def post_image(
    entity_type: ImageEntityEnum,
    image: FileStorage
):
    """
    """
    if entity_type == ImageEntityEnum.product_image:
        pass
    elif entity_type == ImageEntityEnum.product_logo:
        pass
    elif entity_type == ImageEntityEnum.variant_image:
        pass
    else:
        InvalidProcess("invalid image entity")

    image_utils.process_image_upload(image)
