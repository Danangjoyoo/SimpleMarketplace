"""
Image Logic Controllers
"""
from chain_logging.flask import logger
from werkzeug.datastructures import FileStorage

from app.queries import as_dict
from app.queries.variant_query import select_specific_variant
from app.queries.product_query import select_specific_product
from app.queries.image_query import insert_image, update_image, register_image_collection, delete_from_image
from app.schema.image_schema import ImageEntityEnum
from app.utils import image_utils
from app.utils.exception import InvalidProcess


def put_product_logo(product_id: int, image_file: FileStorage):
    try:
        product = select_specific_product(product_id)

        if not product:
            raise InvalidProcess(f"product not found {product_id=}")

        image_url = image_utils.process_image_upload(image_file)
        update_image(product.logo_id, image_url)

        return {"status": 1}

    except Exception as error:
        logger.error(f"failed to update product logo {product_id=} : {error}")
        if isinstance(error, InvalidProcess):
            raise error
        raise InvalidProcess(f"failed to update product logo")


def post_product_image_collection(product_id: int, image_file: FileStorage):
    try:
        product = select_specific_product(product_id)

        if not product:
            raise InvalidProcess(f"product not found {product_id=}")

        image_url = image_utils.process_image_upload(image_file)
        new_image = insert_image(image_url)
        register_image_collection(product.images, new_image.id)
        new_image = as_dict(new_image)

        return new_image

    except Exception as error:
        logger.error(f"failed to add product image collection {product_id=} : {error}")
        if isinstance(error, InvalidProcess):
            raise error
        raise InvalidProcess(f"failed to add product image collection")


def post_variant_image_collection(variant_id: int, image_file: FileStorage):
    try:
        variant = select_specific_variant(variant_id)

        if not variant:
            raise InvalidProcess(f"variant not found {variant_id=}")

        image_url = image_utils.process_image_upload(image_file)
        new_image = insert_image(image_url)
        register_image_collection(variant.images, new_image.id)
        new_image = as_dict(new_image)

        return new_image

    except Exception as error:
        logger.error(f"failed to add variant image collection {variant_id=} : {error}")
        if isinstance(error, InvalidProcess):
            raise error
        raise InvalidProcess(f"failed to add variant image collection")


def delete_image(image_id: int):
    try:
        delete_from_image(image_id)

        return {"status": 1}

    except Exception as error:
        logger.error(f"failed to delete image {image_id=} : {error}")
        if isinstance(error, InvalidProcess):
            raise error
        raise InvalidProcess(f"failed to delete image")
