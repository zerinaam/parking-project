from fastapi import APIRouter
from app.db.session import session
from app.models.parking import Parking
from app.schemas.parking import ParkingModel

router = APIRouter()


@router.get("/parking")
async def get_parking():
    return session.query(Parking).all()


@router.get("/parking/{parking_id}")
async def get_parking_by_id(parking_id: int):
    parking = session.query(Parking).filter(Parking.id == parking_id).first()
    return parking


@router.post("/parking")
async def add_parking(parking_model: ParkingModel):
    parking = Parking(
        id=parking_model.id,
        name=parking_model.name,
        location=parking_model.location,
        working_hours=parking_model.working_hours,
        capacity=parking_model.capacity,
        hour_cost=parking_model.hour_cost
    )

    session.add(parking)
    session.commit()

    return "Parking has been added."


@router.put("/parking/{parking_id}")
async def update_parking(parking_id: int, parking_update: ParkingModel):
    parking = session.query(Parking).filter(Parking.id == parking_id).first()

    if parking is None:
        return "Parking with provided id does not exist."

    parking.name = parking_update.name if parking_update.name else parking.name
    parking.location = parking_update.location if parking_update.location else parking.location
    parking.working_hours = parking_update.working_hours if parking_update.working_hours else parking.working_hours
    parking.capacity = parking_update.capacity if parking_update.capacity else parking.capacity
    parking.hour_cost = parking_update.hour_cost if parking_update.hour_cost else parking.hour_cost

    session.commit()
    return "Parking has been updated."


@router.delete("/parking{parking_id}")
async def delete_parking(parking_id: int):
    parking = session.query(Parking).filter(Parking.id == parking_id).first()

    if parking is None:
        return f"Parking with provided id {parking_id} does not exist."

    session.delete(parking)
    session.commit()
    return "Parking has been deleted."


@router.get("/parking/{parking_id}/availability")
async def display_availability(parking_id: int):
    parking = session.query(Parking).filter(Parking.id == parking_id).first()

    if len(parking.tickets) < parking.capacity:
        return f"Parking is occupied {len(parking.tickets)}/{parking.capacity}"

    return "Parking is full."







