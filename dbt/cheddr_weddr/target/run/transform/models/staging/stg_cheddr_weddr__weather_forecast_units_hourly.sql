
  create or replace   view ANALYTICS.CHEDDR_WEDDR.stg_cheddr_weddr__weather_forecast_units_hourly
  
  
  
  
  as (
    with 

src as (
    select * from raw.cheddr_weddr.weather_forecast

),

unload_json as (
    select 
        payload:hourly_units::variant as hourly_units

    from src

),

final as (
    select 
        j.key as field,
        j.value::varchar as units
        
    from unload_json,
        lateral flatten (input => hourly_units) j
)

select * from final
  );

