from http import HTTPStatus

from flask import Blueprint, Response, make_response
from flask.views import MethodView
from sqlalchemy.sql import text

from app.extensions import db

api = Blueprint("api", __name__, url_prefix="/api")


class HealthCheck(MethodView):
    """Health endpoint."""

    def get(self) -> Response:
        """Ensure the system is reachable and the database connection is alive."""

        result = db.session.execute(text("SELECT 1;")).first()
        assert result == (1,)

        return make_response("This system is alive!", HTTPStatus.OK)


api.add_url_rule("/health", view_func=HealthCheck.as_view("health"))
