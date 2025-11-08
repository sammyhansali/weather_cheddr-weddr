with

src as (

    select
        *

    from {{ source('cheddr_weddr', 'flood')}}

),

final as (

    select
        location_id::number as location_id,
        to_date(date, 'MMDDYYYY') as data_date,
        load_ts,
        payload:daily as daily,
        payload:daily_units as daily_units
    
    from src

)

select * from final