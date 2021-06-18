from flask import Blueprint, request, current_app
from http import HTTPStatus

from app.models import CategoriesModel

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
