import os
from enum import Enum


class EnvironmentConfig(str, Enum):
    """Environment config enum."""

    TESTING = "testing"
    DEVELOPMENT = "development"


class Config:
    """Default config values."""

    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
    MYSQL_PORT = os.environ.get("MYSQL_PORT", 3306)
    MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "skinandme")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql://{MYSQL_USER}:{MYSQL_ROOT_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True

    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.db')}"
    )
