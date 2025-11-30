
  create or replace   view ANALYTICS.CHEDDR_WEDDR.stg__air_quality
  
  
  
  
  as (
    with

src as (

    select
        *

    from raw.cheddr_weddr.air_quality

),

final as (

    select
        location_id::number as location_id,
        date::date as data_date,
        load_ts,
        payload:hourly as hourly,
        payload:hourly_units as hourly_units
    
    from src

)

select * from final
  );

