from fastapi import APIRouter
from api.db import get_conn

router = APIRouter()

@router.get("/daily-trends")
def daily_trends():
    conn = get_conn()

    result = conn.execute("""
        SELECT *
        FROM agg_incident_daily
        ORDER BY incident_date DESC
    """).fetchdf()

    return result.to_dict(orient="records")


@router.get("/sla-breaches")
def sla_breaches():
    conn = get_conn()

    result = conn.execute("""
        SELECT severity, sum(sla_breaches) as total_breaches
        FROM agg_incident_daily
        GROUP BY severity
    """).fetchdf()

    return result.to_dict(orient="records")