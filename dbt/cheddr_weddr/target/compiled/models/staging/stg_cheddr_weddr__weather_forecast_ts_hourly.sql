with 

src as (
    select * from raw.cheddr_weddr.weather_forecast

),

final as (
    select 
        payload:hourly::variant as hourly

    from src

)

select * from final