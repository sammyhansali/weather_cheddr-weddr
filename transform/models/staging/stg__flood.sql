with

src as (

    select
        *

    from {{ source('cheddr_weddr', 'flood')}}

),

final as (

    select
        location_id,
        date,
        load_ts,
        payload:daily as daily,
        payload:daily_units as daily_units
    
    from src

)

select * from final