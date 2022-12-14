from app.models import TasksCategoriesModel as TCM, CategoriesModel, TasksModel

from app.services.helpers import add_commit, verify_missing_keys, verify_received_keys

from app.exc import RequiredKeysError, MissingKeysError

# --------------------------------


def create_category_name(payload: dict) -> dict:
    keys_list = ["task_name", "category_name"]

    if verify_missing_keys(payload, keys_list):
        raise MissingKeysError(keys_list, payload)

    if verify_received_keys(payload, keys_list):
        raise RequiredKeysError(keys_list, payload)

    task: TasksModel = TasksModel.query.filter_by(name=payload.get("task_name")).first()
    category: CategoriesModel = CategoriesModel.query.filter_by(name=payload.get("category_name")).first()

    task_category: TCM = TCM(task_id=task.id, category_id=category.id)

    add_commit(task_category)

    return {
        "id": task_category.id,
        "task": task.name,
        "category": category.name,
        "eisenhower_classification": task.eisenhower.type,
    }
