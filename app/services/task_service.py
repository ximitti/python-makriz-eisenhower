from app.models import TasksModel as TM

from app.exc import MissingKeysError, RequiredKeysError, InvalidOptionsError as IOE

from app.services.helpers import (
    eisenhower_classification,
    add_commit,
    verify_missing_keys,
    verify_received_keys,
)

# -------------------------------


def create_task(payload: dict) -> dict:
    keys_list = ["name", "description", "duration", "importance", "urgency"]

    if verify_missing_keys(payload, keys_list):
        raise MissingKeysError(keys_list, payload)

    if verify_received_keys(payload, keys_list):
        raise RequiredKeysError(keys_list, payload)

    importance = payload.get("importance")
    urgency = payload.get("urgency")

    if importance not in IOE.valid_options or urgency not in IOE.valid_options:
        raise IOE(importance=importance, urgency=urgency)

    payload["eisenhower_id"] = eisenhower_classification(importance, urgency)

    task: TM = TM(**payload)

    add_commit(task)

    return {
        "id": task.id,
        "name": task.name,
        "description": task.description,
        "duration": task.duration,
        "eisenhower_classification": task.eisenhower.type,
    }
