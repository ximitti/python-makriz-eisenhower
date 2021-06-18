from flask import Blueprint, request
from http import HTTPStatus

from app.services.category_task_services import create_category_name

from app.exc import MissingKeysError, RequiredKeysError

# -------------------------------------------

bp: Blueprint = Blueprint("bp_tasks_categories", __name__)

# -------------------------------------------


@bp.post("/task_category")
def register_task_category():

    try:
        return create_category_name(request.get_json()), HTTPStatus.CREATED

    except MissingKeysError as e:
        return e.message

    except RequiredKeysError as e:
        return e.message
