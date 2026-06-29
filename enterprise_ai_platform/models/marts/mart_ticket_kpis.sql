with base as (
    select *
    from {{ ref('stg_tickets') }}
),

kpis as (
    select
        ticket_id,
        user_id,
        department,
        priority,
        status,
        issue_type,

        created_at,   -- 🔥 ADD
        resolved_at,  -- (optional but useful)

        satisfaction_score,

        date_diff('minute', created_at, resolved_at) / 60.0 as resolution_time_hours,

        case
            when satisfaction_score < 3 then 1
            else 0
        end as low_satisfaction_flag

    from base
)

select * from kpis