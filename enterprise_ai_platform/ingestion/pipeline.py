import duckdb
import pandas as pd

from ingestion.loaders.json_loader import load_incidents, load_tickets
from ingestion.transformers.normalize_incidents import normalize_incidents
from ingestion.transformers.normalize_tickets import normalize_tickets
from ingestion.config import WAREHOUSE_PATH


def run_pipeline():

    print("\n🚀 Starting ingestion pipeline...")

    conn = duckdb.connect(WAREHOUSE_PATH)

    incidents = load_incidents()
    tickets = load_tickets()

    print(f"Loaded {len(incidents)} incidents")
    print(f"Loaded {len(tickets)} tickets")

    incidents_clean = normalize_incidents(incidents)
    tickets_clean = normalize_tickets(tickets)

    incidents_df = (
    pd.DataFrame(incidents_clean)
    .drop_duplicates(subset=["id"])
    )

    tickets_df = (
    pd.DataFrame(tickets_clean)
    .drop_duplicates(subset=["id"])
    )
    print("\n🔍 Deduplication Summary")

    print(
    f"Incidents: {len(incidents_clean)} → {len(incidents_df)}"
    )

    print(
    f"Tickets: {len(tickets_clean)} → {len(tickets_df)}"
    )
    # Data quality checks
    missing_user_ids = sum(
        1 for t in tickets if "user_id" not in t
    )

    print(f"\n🔍 Tickets missing user_id: {missing_user_ids}")


    # Register DataFrames
    conn.register("incidents_df", incidents_df)
    conn.register("tickets_df", tickets_df)

    # Rebuild tables
    conn.execute("DROP TABLE IF EXISTS incidents")
    conn.execute("DROP TABLE IF EXISTS tickets")

    conn.execute("""
        CREATE TABLE incidents AS
        SELECT *
        FROM incidents_df
    """)

    conn.execute("""
        CREATE TABLE tickets AS
        SELECT *
        FROM tickets_df
    """)

    incident_count = conn.execute(
        "SELECT COUNT(*) FROM incidents"
    ).fetchone()[0]

    ticket_count = conn.execute(
        "SELECT COUNT(*) FROM tickets"
    ).fetchone()[0]

    print("\n📦 Tables created successfully!")

    print(f"📊 Incidents count: {incident_count}")
    print(f"🎫 Tickets count: {ticket_count}")

    conn.close()

    print("\n✅ Pipeline executed successfully!")


if __name__ == "__main__":
    run_pipeline()