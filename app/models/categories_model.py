from app import db
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship, backref

# --------------------------------


class CategoriesModel(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    tasks = relationship("TasksModel", secondary="tasks_categories", backref=backref("categories"))
