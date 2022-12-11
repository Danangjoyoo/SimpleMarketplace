"""
Database Connection
"""
import os
from flask import Flask, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from werkzeug.local import LocalProxy


database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)
DBSession = sessionmaker(bind=engine, autocommit=False)


def open_session():
    """
    open database session
    """
    with DBSession() as sess:
        g.db_session = sess


def close_session(response):
    """
    close database session
    """
    g.db_session.close()
    return response


def setup_database_middleware(app: Flask):
    """
    Setup database middleware to open the session for every request coming
    and close after request is finished
    """
    app.before_request(open_session)
    app.after_request(close_session)


def get_db_session():
    """
    Get database session under request context.
    """
    if not "db_session" in vars(g):
        open_session()
    return g.db_session


session: Session = LocalProxy(get_db_session)
"""
database session pointer

Since flask is using thread-based request and utilizing its isolated environment for each request,
the object pointed from here is always localized for its thread only
"""
