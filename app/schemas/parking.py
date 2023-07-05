from pydantic import BaseModel


class ParkingModel(BaseModel):
    id: int | None
    name: str | None
    location: str | None
    working_hours: str | None
    capacity: int | None
    hour_cost: int | None
