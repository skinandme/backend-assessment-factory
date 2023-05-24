import pytest

from app.entrypoint import create_app
from app.extensions import db
from app.config import EnvironmentConfig


@pytest.fixture(scope="session", autouse=True)
def app():
    flask_app = create_app(env=EnvironmentConfig.TESTING)
    db.app = flask_app

    with flask_app.app_context():
        db.create_all()

    yield flask_app

    with flask_app.app_context():
        db.drop_all()


@pytest.fixture(autouse=True)
def session(app):
    context = app.app_context()
    context.push()

    for table in reversed(db.metadata.sorted_tables):
        db.session.execute(table.delete())

    yield

    db.session.rollback()
    context.pop()
