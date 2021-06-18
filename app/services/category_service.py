from app import db

from app.exc import MissingKeysError, RequiredKeysError

from app.services.helpers import add_commit, verify_missing_keys, verify_received_keys

from app.models import CategoriesModel as CM, TasksModel as TM, TasksCategoriesModel as TCM

# ---------------------------------------------


def create_category(payload: dict) -> dict:
    keys_list = ["name", "description"]

    if verify_missing_keys(payload, keys_list):
        raise MissingKeysError(keys_list, payload)

    if verify_received_keys(payload, keys_list):
        raise RequiredKeysError(keys_list, payload)

    new_category = CM(**payload)

    add_commit(new_category)

    return {"id": new_category.id, "name": new_category.name, "description": new_category.description}


def select_categories() -> list:
    category_list: list[CM] = db.session.query(CM).all()

    task_list: list[tuple[CM, TM]] = db.session.query(CM, TM).select_from(CM).join(TCM).join(TM).all()

    return [
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
