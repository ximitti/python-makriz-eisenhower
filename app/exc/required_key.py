from http import HTTPStatus

# ----------------------------


class RequiredKeysError(Exception):
    def __init__(self, key_list: list, payload: dict) -> None:

        self.message = (
            {"error": {"required keys": key_list, "received keys": list(payload.keys())}},
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
