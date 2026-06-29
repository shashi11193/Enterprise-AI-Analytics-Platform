select
    department,

    count(*) as total_tickets,

    avg(resolution_time_hours) as avg_resolution_time,

    avg(satisfaction_score) as avg_satisfaction,

    sum(low_satisfaction_flag) as low_satisfaction_cases

from {{ ref('mart_ticket_kpis') }}

group by 1