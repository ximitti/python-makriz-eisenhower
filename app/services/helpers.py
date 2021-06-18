from app.models import EisenhowersModel

# ---------------------------


def eisenhower_classification(importance: int, urgency: int) -> int:
    classification_list = [
        {"importance": 1, "urgency": 1, "classification": "Do It First"},
        {"importance": 1, "urgency": 2, "classification": "Delegate It"},
        {"importance": 2, "urgency": 1, "classification": "Schedule It"},
        {"importance": 2, "urgency": 2, "classification": "Delete It"},
    ]

    for classification in classification_list:

        if classification["importance"] == importance and classification["urgency"] == urgency:

            eisenhower = EisenhowersModel.query.filter_by(type=classification["classification"]).first()

            return eisenhower.id
