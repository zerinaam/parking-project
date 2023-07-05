from pydantic import BaseModel
from pydantic.schema import datetime


class TicketModel(BaseModel):
    id: int | None
    created_at: datetime | None
    registration: str | None
    parking_id: int | None
