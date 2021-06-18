from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

from app.exc import InvalidOptionsError, MissingKeysError, RequiredKeysError

from app.services.task_service import create_task

# ---------------------------------

bp: Blueprint = Blueprint("bp_tasks", __name__)

# ---------------------------------


@bp.post("/task")
def register_task():

    try:
        return create_task(request.get_json()), HTTPStatus.CREATED

    except IntegrityError as e:
        return {"error": f"duplicate key: {e.params['name']}"}, HTTPStatus.BAD_REQUEST

    except InvalidOptionsError as e:
        return e.message

    except MissingKeysError as e:
        return e.message

    except RequiredKeysError as e:
        return e.message
