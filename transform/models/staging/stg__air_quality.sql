with

src as (

    select
        *

    from {{ source('cheddr_weddr', 'air_quality')}}

),

final as (

    select
        location_id,
        date,
        load_ts,
        payload:hourly as hourly,
        payload:hourly_units as hourly_units
    
    from src

)

select * from final