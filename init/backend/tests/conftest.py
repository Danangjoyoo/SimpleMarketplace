import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.connection import Base
from wsgi import application

database_url = "sqlite:///./database/app.db"

sync_engine = create_engine(database_url, echo=True, future=True)
sync_session = sessionmaker(bind=sync_engine, autocommit=False, expire_on_commit=False)

@pytest.fixture
def app():
    application.config.update({"TESTING": True})
    Base.metadata.create_all(sync_engine)
    yield application
    Base.metadata.drop_all(sync_engine)

@pytest.fixture
def client(app):
    return application.test_client()