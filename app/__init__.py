from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from environs import Env

from app import views

# -----------------------
db: SQLAlchemy = SQLAlchemy()
mg: Migrate = Migrate()

env: Env = Env()
env.read_env()

# -----------------------


def create_app() -> Flask:

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    db.init_app(app)
    app.db = db

    from app.models import CategoriesModel, EisenhowersModel, TasksCategoriesModel, TasksModel

    mg.init_app(app, db)

    views.init_app(app)

    return app
