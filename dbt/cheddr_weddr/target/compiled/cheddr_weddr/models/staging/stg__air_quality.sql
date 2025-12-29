with

src as (

    select *

    from raw.cheddr_weddr.air_quality

),

final as (

    select
        w.location_ids[f.index]::number as location_id,
        w.date::date as data_date,
        w.load_ts,
        f.value:hourly as hourly,
        f.value:hourly_units as hourly_units

    from src as w,
        lateral flatten(input => w.payload) as f

)

select * from final