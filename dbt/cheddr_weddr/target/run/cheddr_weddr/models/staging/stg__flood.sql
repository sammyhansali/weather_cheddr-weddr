
  create or replace   view ANALYTICS.CHEDDR_WEDDR.stg__flood
  
  
  
  
  as (
    with

src as (

    select
        *

    from raw.cheddr_weddr.flood

),

final as (

    select
        location_id::number as location_id,
        date::date as data_date,
        load_ts,
        payload:daily as daily,
        payload:daily_units as daily_units
    
    from src

)

select * from final
  );

