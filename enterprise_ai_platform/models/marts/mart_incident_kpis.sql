with base as (
    select *
    from {{ ref('stg_incidents') }}
),

kpis as (
    select
        incident_id,
        service,
        severity,
        owner_team,
        status,

        created_at,   -- 🔥 ADD THIS BACK

        response_time_minutes,

        date_diff('minute', created_at, resolved_at) / 60.0 as resolution_time_hours,

        case 
            when severity = 'SEV1' and response_time_minutes > 30 then 1
            when severity = 'SEV2' and response_time_minutes > 60 then 1
            when severity = 'SEV3' and response_time_minutes > 240 then 1
            else 0
        end as sla_breach_flag

    from base
)

select * from kpis