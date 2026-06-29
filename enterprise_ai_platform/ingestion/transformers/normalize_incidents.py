def normalize_incidents(data):
    normalized = []

    for item in data:
        normalized.append({
            "id": item["incident_id"],
            "type": item["incident_type"],
            "severity": item["severity"],
            "service": item["service_affected"],
            "owner_team": item["owner_team"],
            "response_time": item["response_time_minutes"],
            "root_cause": item["root_cause"],
            "created_at": item["created_at"],
            "resolved_at": item["resolved_at"],
            "status": item["status"]
        })

    return normalized