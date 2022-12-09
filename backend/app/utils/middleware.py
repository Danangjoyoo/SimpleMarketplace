"""
Middleware Utils
"""
from flask import Flask, g
from app.database.connection import session_opener


def database_middleware(app: Flask):
    """
    """
    @app.before_request
    def open_session():
        with session_opener() as sess:
            g.db_session = sess

    @app.after_request
    def close_session():
        g.db_session.close()
