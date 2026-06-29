from fastapi import APIRouter
from api.db import get_conn

router = APIRouter()

@router.get("/daily-trends")
def ticket_trends():
    conn = get_conn()

    result = conn.execute("""
        SELECT *
        FROM agg_ticket_daily
        ORDER BY ticket_date DESC
    """).fetchdf()

    return result.to_dict(orient="records")


@router.get("/department-performance")
def dept_perf():
    conn = get_conn()

    result = conn.execute("""
        SELECT *
        FROM agg_department_performance
        ORDER BY avg_satisfaction DESC
    """).fetchdf()

    return result.to_dict(orient="records")