import pytest


# from app import create_app
from main import app as flask_app, db
# from main import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def init_database():
    # Create the database and the database table
    db.create_all()
    yield db  # this is where the testing happens!
    db.drop_all()
