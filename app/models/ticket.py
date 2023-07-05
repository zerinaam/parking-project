from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    registration = Column(String)

    parking_id = Column(Integer, ForeignKey("parking.id"))
    parking = relationship("Parking", backref ="tickets")

    tickets = []
