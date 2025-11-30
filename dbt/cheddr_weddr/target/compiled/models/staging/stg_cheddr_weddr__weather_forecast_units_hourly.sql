with 

src as (
    select * from raw.cheddr_weddr.weather_forecast

),

final as (
    select 
        payload:hourly_units::variant as hourly_units

    from src

)

select * from final