select
    id as incident_id,

    case
    when upper(severity) in ('SEV1','SEV-1','SEV 1','CRITICAL') then 'SEV1'
    when upper(severity) in ('SEV2','SEV-2','SEV 2','HIGH') then 'SEV2'
    when upper(severity) in ('SEV3','SEV-3','SEV 3','MEDIUM') then 'SEV3'
    else 'SEV3'
end as severity,

    service,
    owner_team,

    response_time as response_time_minutes,

    root_cause,

    cast(created_at as timestamp) as created_at,
    cast(resolved_at as timestamp) as resolved_at,

    status

from {{ source('bronze', 'incidents') }}