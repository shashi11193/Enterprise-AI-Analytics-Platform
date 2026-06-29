def normalize_tickets(data):
    normalized = []

    for item in data:

        normalized.append({
            "id": item.get("ticket_id"),
            "user_id": item.get("user_id", "UNKNOWN"),
            "department": item.get("department", "UNKNOWN"),
            "priority": item.get("priority", "LOW"),
            "status": item.get("status", "OPEN"),
            "issue_type": item.get("issue_type", "UNKNOWN"),
            "linked_incident": item.get("linked_incident"),
            "satisfaction_score": item.get("satisfaction_score"),
            "created_at": item.get("created_at"),
            "resolved_at": item.get("resolved_at")
        })

    return normalized