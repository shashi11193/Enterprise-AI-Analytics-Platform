select
    id as ticket_id,

    user_id,
    department,

    case
    when lower(priority) in ('low','p3') then 'Low'
    when lower(priority) in ('medium','p2') then 'Medium'
    when lower(priority) in ('high','p1','urgent') then 'High'
    else 'Medium'
end as priority,

    status,
    issue_type,
    linked_incident,
    satisfaction_score,

    cast(created_at as timestamp) as created_at,
    cast(resolved_at as timestamp) as resolved_at

from {{ source('bronze', 'tickets') }}