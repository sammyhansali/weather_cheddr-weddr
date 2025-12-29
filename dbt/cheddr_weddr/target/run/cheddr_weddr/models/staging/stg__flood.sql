
  create or replace   view DEV.CHEDDR_WEDDR.stg__flood
  
  
  
  
  as (
    with

src as (

    select *

    from raw.cheddr_weddr.flood

),

final as (

    select
        w.location_ids[f.index]::number as location_id,
        w.date::date as data_date,
        w.load_ts,
        f.value:daily as daily,
        f.value:daily_units as daily_units

    from src as w,
        lateral flatten(input => w.payload) as f

)

select * from final
  );

