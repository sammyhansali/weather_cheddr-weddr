
  
    

create or replace transient table ANALYTICS.CHEDDR_WEDDR.dim_cheddr_weddr__weather_forecast_units_daily
    
    
    
    as (with 

stg as (
    select daily_units 
    from ANALYTICS.CHEDDR_WEDDR.stg_cheddr_weddr__weather_forecast

),

final as (
    select 
        j.key as field,
        j.value::varchar as units
        
    from stg,
        lateral flatten (input => daily_units) j
)

select * from final
    )
;


  