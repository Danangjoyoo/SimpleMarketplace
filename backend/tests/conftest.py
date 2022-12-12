import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from app.database.models import Base
from app.database.connection import DBSession
from wsgi import application

database_url = "sqlite:///./tests/test.db"

sync_engine = create_engine(database_url)
sync_session = sessionmaker(bind=sync_engine, autocommit=False, expire_on_commit=False)

@pytest.fixture
def app():
    @event.listens_for(Engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

    application.config.update({"TESTING": True})
    DBSession = sync_session
    Base.metadata.create_all(sync_engine)
    yield application
    Base.metadata.drop_all(sync_engine)

@pytest.fixture
def client(app):
    return application.test_client()