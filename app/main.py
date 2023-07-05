from fastapi import FastAPI

from app.routers import parking, ticket

app = FastAPI(
    title="Parking",
    version="0.1.0",
)

app.include_router(parking.router)
app.include_router(ticket.router)
