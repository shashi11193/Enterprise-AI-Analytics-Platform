select
    cast(created_at as date) as incident_date,
    severity,
    service,

    count(*) as total_incidents,

    avg(response_time_minutes) as avg_response_time,

    avg(resolution_time_hours) as avg_resolution_time,

    sum(sla_breach_flag) as sla_breaches

from {{ ref('mart_incident_kpis') }}

group by 1, 2, 3