from app import db
from app.models import EisenhowersModel as EM

# ---------------------------


def add_commit(model: db.Model) -> None:
    db.session.add(model)
    db.session.commit()


def eisenhower_classification(importance: int, urgency: int) -> int:
    classification_list = [
        {"importance": 1, "urgency": 1, "classification": "Do It First"},
        {"importance": 1, "urgency": 2, "classification": "Delegate It"},
        {"importance": 2, "urgency": 1, "classification": "Schedule It"},
        {"importance": 2, "urgency": 2, "classification": "Delete It"},
    ]

    for classification in classification_list:

        if classification["importance"] == importance and classification["urgency"] == urgency:

            eisenhower: EM = EM.query.filter_by(type=classification["classification"]).first()

            return eisenhower.id


def verify_missing_keys(payload: dict, required_keys: list) -> list:
    payload_keys = payload.keys()

    return [key for key in required_keys if key not in payload_keys]


def verify_received_keys(payload: dict, key_list: list) -> list:
    payload_key = payload.keys()

    return [key for key in payload_key if key not in key_list]
