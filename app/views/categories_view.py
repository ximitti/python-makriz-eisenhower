from flask import Blueprint, request, current_app, jsonify
from http import HTTPStatus
from ipdb import set_trace

from app.models import CategoriesModel, TasksModel, TasksCategoriesModel as TCM


# --------------------------------------

bp: Blueprint = Blueprint("bp_categories", __name__)

# --------------------------------------


@bp.post("/category")
def create_category():
    session = current_app.db.session

    payload = request.get_json()

    category: CategoriesModel = CategoriesModel(**payload)

    session.add(category)
    session.commit()

    return {"id": category.id, "name": category.name, "description": category.description}, HTTPStatus.CREATED


@bp.get("/")
def get_all():
    session = current_app.db.session

    category_list: list[CategoriesModel] = session.query(CategoriesModel).all()

    task_list: list[tuple[CategoriesModel, TasksModel]] = (
        session.query(CategoriesModel, TasksModel).select_from(CategoriesModel).join(TCM).join(TasksModel).all()
    )

    output = [
        {
            "category": {
                "name": category.name,
                "description": category.description,
                "task": [
                    {"name": task.name, "description": task.description, "priority": task.eisenhower.type}
                    for cat, task in task_list
                    if cat.id == category.id
                ],
            }
        }
        for category in category_list
    ]

    return jsonify(output)
