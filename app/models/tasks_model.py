from app import db
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

# ---------------------------


class TasksModel(db.Model):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)

    eisenhower_id = Column(Integer, ForeignKey("eisenhowers.id"), nullable=False, unique=True)

    eisenhower = relationship("EisenhowersModel", backref=backref("task"))
