from flask import Blueprint, request, current_app
from http import HTTPStatus

from app.models import TasksCategoriesModel as TCM

# -------------------------------------------

bp: Blueprint = Blueprint("bp_tasks_categories", __name__)

# -------------------------------------------


@bp.post("/task_category")
def create_task_category():
    session = current_app.db.session

    payload = request.get_json()

    task_category: TCM = TCM(**payload)

    session.add(task_category)
    session.commit()

    return {
        "id": task_category.id,
        "task": task_category.tasks.name,
        "category": task_category.categories.name,
        "eisenhower_classification": task_category.tasks.type,
    }, HTTPStatus.CREATED
