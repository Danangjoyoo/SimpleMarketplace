"""
Storage app
"""
import os
from flask import Flask
from flask_toolkits import AutoSwagger

from app.storage import storage_router

def make_app():
    """
    Application Factory
    """
    app = Flask(__name__)

    apidocs = AutoSwagger("Storage Service")

    app.register_blueprint(apidocs)
    app.register_blueprint(storage_router)


    return app