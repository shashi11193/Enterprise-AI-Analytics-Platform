from ingestion.loaders.json_loader import (
    load_incidents,
    load_tickets,
)

incidents = load_incidents()
tickets = load_tickets()

print("\n=== INCIDENT AUDIT ===")
print("Total incidents:", len(incidents))

incident_ids = [i.get("incident_id") for i in incidents]

print("Unique incident IDs:", len(set(incident_ids)))

duplicates = [
    x
    for x in set(incident_ids)
    if incident_ids.count(x) > 1
]

print("Duplicate incident IDs:", duplicates)

print("\n=== TICKET AUDIT ===")
print("Total tickets:", len(tickets))

ticket_ids = [t.get("ticket_id") for t in tickets]

print("Unique ticket IDs:", len(set(ticket_ids)))

duplicates = [
    x
    for x in set(ticket_ids)
    if ticket_ids.count(x) > 1
]

print("Duplicate ticket IDs:", duplicates)

missing_user_ids = sum(
    1
    for t in tickets
    if "user_id" not in t
)

print("Tickets missing user_id:", missing_user_ids)