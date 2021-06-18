from app import db
from sqlalchemy import Column, Integer, ForeignKey

# ---------------------------


class TasksCategoriesModel(db.Model):
    __tablename__ = "tasks_categories"

    id = Column(Integer, primary_key=True)

    task_id = Column(Integer, ForeignKey("tasks.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
