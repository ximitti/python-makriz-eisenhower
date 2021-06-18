from http import HTTPStatus

# -----------------------------


class InvalidOptionsError(Exception):
    valid_options = [1, 2]

    def __init__(self, importance: int, urgency: int) -> None:

        self.message = (
            {
                "error": {
                    "valid options": {"importance": self.valid_options, "urgency": self.valid_options},
                    "received options": {"importance": importance, "urgency": urgency},
                }
            },
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
