"""
View Function Collections
"""
from flask_toolkits import APIRouter
from app.views import image_view, product_view, variant_view

# Routers
image_router = APIRouter("image", __name__, url_prefix="/image", tags=["Image"])
product_router = APIRouter("product", __name__, url_prefix="/product", tags=["Product"])
variant_router = APIRouter("variant", __name__, url_prefix="/variant", tags=["Variant"])

# Image Endpoints
image_router.add_url_rule("/add", view_func=image_view.create_image_view, methods=["POST"])
image_router.add_url_rule("/delete/<int:image_id>", view_func=image_view.delete_image_view, methods=["DELETE"])

# Product Endpoints
product_router.add_url_rule("", view_func=product_view.get_product_list_view, methods=["GET"])
product_router.add_url_rule("/<int:product_id>", view_func=product_view.get_product_view, methods=["GET"])
product_router.add_url_rule("/add", view_func=product_view.create_product_view, methods=["POST"])
product_router.add_url_rule("/update/<int:product_id>", view_func=product_view.update_product_view, methods=["PUT"])
product_router.add_url_rule("/delete/<int:product_id>", view_func=product_view.delete_product_view, methods=["DELETE"])

# Variant Endpoints
variant_router.add_url_rule("", view_func=variant_view.get_variant_list_view, methods=["GET"])
variant_router.add_url_rule("/<int:variant_id>", view_func=variant_view.get_variant_view, methods=["GET"])
variant_router.add_url_rule("/add", view_func=variant_view.create_variant_view, methods=["POST"])
variant_router.add_url_rule("/update/<int:variant_id>", view_func=variant_view.update_variant_view, methods=["PUT"])
variant_router.add_url_rule("/delete/<int:variant_id>", view_func=variant_view.delete_variant_view, methods=["DELETE"])
