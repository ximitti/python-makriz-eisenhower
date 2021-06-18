from flask import Blueprint, request, jsonify
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.exc import MissingKeysError, RequiredKeysError

from app.services.category_service import create_category, select_categories


# --------------------------------------

bp: Blueprint = Blueprint("bp_categories", __name__)

# --------------------------------------


@bp.post("/category")
def register_category():

    try:
        return create_category(request.get_json()), HTTPStatus.CREATED

    except IntegrityError as e:
        return {"error": f"duplicate key: {e.params['name']}"}, HTTPStatus.BAD_REQUEST

    except MissingKeysError as e:
        return e.message

    except RequiredKeysError as e:
        return e.message


@bp.get("/")
def get_all():

    return jsonify(select_categories()), HTTPStatus.OK
