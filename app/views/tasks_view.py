from flask import Blueprint, request, current_app
from http import HTTPStatus

from app.models import TasksModel

from app.services.helpers import eisenhower_classification

# ---------------------------------

bp: Blueprint = Blueprint("bp_tasks", __name__)

# ---------------------------------


@bp.post("/task")
def create_task():
    session = current_app.db.session

    payload = request.get_json()

    payload["eisenhower_id"] = eisenhower_classification(payload.get("importance"), payload.get("urgency"))

    task: TasksModel = TasksModel(**payload)

    session.add(task)
    session.commit()

    return {
        "id": task.id,
        "name": task.name,
        "description": task.description,
        "duration": task.duration,
        "eisenhower_classification": task.eisenhower.type,
    }, HTTPStatus.CREATED
