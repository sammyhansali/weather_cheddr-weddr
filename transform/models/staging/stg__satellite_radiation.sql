with

src as (

    select
        *

    from {{ source('cheddr_weddr', 'satellite_radiation')}}

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