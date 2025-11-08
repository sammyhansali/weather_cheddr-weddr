with

src as (

    select
        *

    from {{ source('cheddr_weddr', 'weather')}}

),

final as (

    select
        location_id::number as location_id,
        to_date(date, 'MMDDYYYY') as data_date,
        load_ts,
        payload:hourly as hourly,
        payload:hourly_units as hourly_units
    
    from src

)

select * from final