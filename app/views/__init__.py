from flask import Flask


# ------------------------------


def init_app(app: Flask) -> None:
    from .categories_view import bp as bp_categories

    app.register_blueprint(bp_categories)

    from .tasks_view import bp as bp_tasks

    app.register_blueprint(bp_tasks)

    from .tasks_categories_view import bp as bp_tasks_categories

    app.register_blueprint(bp_tasks_categories)
