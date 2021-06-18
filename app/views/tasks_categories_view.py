from flask import Blueprint, request, current_app
from http import HTTPStatus
from ipdb import set_trace

from app.models import TasksCategoriesModel as TCM, CategoriesModel, TasksModel

# -------------------------------------------

bp: Blueprint = Blueprint("bp_tasks_categories", __name__)

# -------------------------------------------


@bp.post("/task_category")
def create_task_category():
    session = current_app.db.session

    payload = request.get_json()

    task: TasksModel = TasksModel.query.filter_by(name=payload.get("task_name")).first()
    category: CategoriesModel = CategoriesModel.query.filter_by(name=payload.get("category_name")).first()

    task_category: TCM = TCM(task_id=task.id, category_id=category.id)

    session.add(task_category)
    session.commit()

    return {
        "id": task_category.id,
        "task": task.name,
        "category": category.name,
        "eisenhower_classification": task.eisenhower.type,
    }, HTTPStatus.CREATED
