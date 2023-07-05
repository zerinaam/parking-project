import datetime

from fastapi import APIRouter
from app.db.session import session
from app.models.parking import Parking
from app.models.ticket import Ticket
from app.schemas.ticket import TicketModel

router = APIRouter()


@router.get("/ticket")
async def get_tickets():
    return session.query(Ticket).all()


@router.get("/ticket/{ticket_id}")
async def get_ticket_by_id(ticket_id: int):
    ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        return "Ticket with provided id does not exist."
    return ticket


@router.post("/ticket")
async def add_ticket(ticket_model: TicketModel):
    ticket = Ticket(
        id=ticket_model.id,
        created_at=ticket_model.created_at,
        registration=ticket_model.registration,
        parking_id=ticket_model.parking_id
    )

    session.add(ticket)
    session.commit()

    parking = session.query(Ticket).filter(Ticket.id == ticket.id).first()
    parking.tickets.append(ticket)

    return "Ticket has been added."


@router.put("/ticket/{ticket_id}")
async def update_ticket(ticket_id: int, ticket_update: TicketModel):
    ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()

    if ticket is None:
        return "Ticket with provided id does not exist."

    ticket.created_at = ticket_update.created_at if ticket_update.created_at else ticket.created_at
    ticket.registration = ticket_update.registration if ticket_update.registration else ticket.registration
    ticket.parking_id = ticket_update.parking_id if ticket_update.parking_id else ticket.parking_id

    session.commit()
    return "Ticket has been updated."


@router.delete("/ticket/{ticket_id}")
async def delete_ticket(ticket_id: int):
    ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()

    if ticket is None:
        return f"Ticket with provided id {ticket_id} does not exist."

    session.delete(ticket)
    session.commit()
    return "Ticket has been deleted."


@router.get("/parking/{parking_id}/ticket/{ticket_id}/price")
async def get_ticket_price(parking_id: int, ticket_id: int):
    parking = session.query(Parking).filter(Parking.id == parking_id).first()
    ticket = session.query(Ticket).filter(Ticket.id == ticket_id).first()

    time_on_parking = datetime.datetime.now() - ticket.created_at
    duration_in_s = time_on_parking.total_seconds()
    hours = duration_in_s // 3600
    price = (hours + 1) * parking.hour_cost

    return price




