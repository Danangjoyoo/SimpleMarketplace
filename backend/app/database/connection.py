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
    """
    g.db_session = DBSession()


def close_session(response):
    """
    """
    g.db_session.close()
    return response


def database_middleware(app: Flask):
    """
    """
    app.before_request(open_session)
    app.after_request(close_session)

def get_db_session():
    """
    """
    if not "db_session" in vars(g):
        open_session()
    return g.db_session

session: Session = LocalProxy(get_db_session)
