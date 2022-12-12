import pytest
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

# load environment
load_dotenv("./tests/.env")

# application setup
from app import make_app
from app.database.models import Base

application = make_app("./tests/.env")
sync_engine = create_engine(os.getenv("DATABASE_URL"))
sync_session = sessionmaker(bind=sync_engine, autocommit=False, expire_on_commit=False)


@pytest.fixture
def app():
    @event.listens_for(Engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

    application.config.update({"TESTING": True})
    Base.metadata.create_all(sync_engine)
    yield application
    Base.metadata.drop_all(sync_engine)

@pytest.fixture
def client(app):
    return application.test_client()