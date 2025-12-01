with

src as (

    select
        *

    from {{ source('cheddr_weddr', 'flood')}}

),

final as (

    -- select
    --     location_id::number as location_id,
    --     date::date as data_date,
    --     load_ts,
    --     payload:daily as daily,
    --     payload:daily_units as daily_units
    
    -- from src

    select 
        w.location_ids[f.index]::number as location_id,
        w.date::date as data_date,
        w.load_ts,
        f.value:daily as daily,
        f.value:daily_units as daily_units,
        
    from src as w,
        lateral flatten (input => w.payload) as f

)

select * from final