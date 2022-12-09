"""
Appication Main File
"""
from chain_logging.flask import setup_chained_logger
from dotenv import load_dotenv
from flask import Flask
from flask_toolkits import AutoSwagger

# load env file before load module files
load_dotenv("/base/app/.env")

from app.database import Base, engine, database_middleware
from app.views import image_router, product_router, variant_router


def make_app():
    """
    Application Factory
    """

    # import required file
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # instantiate application
    app = Flask(__name__)

    # setup middleware
    database_middleware(app)
    setup_chained_logger(app)

    # swagger documentation
    apidocs = AutoSwagger(
        title="Marketplace API Docs",
        description="API Documentation for Product, Variant and Image Endpoints",
        servers=["http://localhost:9000"]
    )

    # register blueprints
    app.register_blueprint(apidocs)
    app.register_blueprint(image_router)
    app.register_blueprint(product_router)
    app.register_blueprint(variant_router)

    return app
