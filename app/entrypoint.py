import logging

from flask import Flask

from app.api import api
from app.config import EnvironmentConfig
from app.extensions import db


def create_app(env: str) -> Flask:
    """Application factory."""

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [sev %(levelno)s] [%(levelname)s] [%(name)s]> %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S",
    )

    app = Flask(__name__)

    conf = _load_configuration(env)
    app.config.from_object(conf)

    _register_extensions(app)

    with app.app_context():
        _register_blueprints(app)
        db.create_all()

    return app


def _load_configuration(env: str) -> str:
    """Load application configuration."""

    configurations = {
        EnvironmentConfig.TESTING.value: "app.config.TestingConfig",
        EnvironmentConfig.DEVELOPMENT.value: "app.config.Config",
    }

    conf = configurations.get(env)
    if not conf:
        raise RuntimeError(f"Could not load configuration {env=}")

    return conf


def _register_blueprints(app: Flask) -> None:
    """Register application blueprints."""

    app.register_blueprint(api)


def _register_extensions(app: Flask) -> None:
    """Register application extensions."""

    db.init_app(app)
