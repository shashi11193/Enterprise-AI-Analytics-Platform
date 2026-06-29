from fastapi import FastAPI
from api.routes import incidents, tickets, analytics

app = FastAPI(title="Enterprise AI Data Platform")

app.include_router(incidents.router, prefix="/incidents")
app.include_router(tickets.router, prefix="/tickets")
app.include_router(analytics.router, prefix="/analytics")

@app.get("/")
def root():
    return {"message": "Enterprise AI Data Platform API is running"}