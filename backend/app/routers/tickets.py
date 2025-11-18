from fastapi import APIRouter, Body
from typing import List, Dict

router = APIRouter()

tickets: List[Dict] = []


@router.post("/tickets/create")
def create_ticket(ticket: Dict = Body(...)):
    print(f"New trouble ticket received: {ticket}")
    tickets.append(ticket)
    return {"message": "Ticket logged successfully", "ticket": ticket}


@router.get("/tickets/count")
def get_ticket_count():
    return {"ticket_count": len(tickets)}
