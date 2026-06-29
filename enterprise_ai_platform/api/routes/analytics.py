from fastapi import APIRouter
from api.db import get_conn

router = APIRouter()

@router.get("/summary")
def summary():
    conn = get_conn()

    incidents = conn.execute("""
        SELECT COUNT(*) as total_incidents
        FROM stg_incidents
    """).fetchone()[0]

    tickets = conn.execute("""
        SELECT COUNT(*) as total_tickets
        FROM stg_tickets
    """).fetchone()[0]

    return {
        "total_incidents": incidents,
        "total_tickets": tickets
    }