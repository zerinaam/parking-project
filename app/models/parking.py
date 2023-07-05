from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Parking(Base):
    __tablename__ = "parking"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    working_hours = Column(String)
    capacity = Column(Integer)
    hour_cost = Column(Integer)

    tickets = [relationship("Ticket", backref ="parking")]

