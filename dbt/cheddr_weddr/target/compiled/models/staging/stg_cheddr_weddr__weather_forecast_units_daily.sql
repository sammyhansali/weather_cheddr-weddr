with 

src as (
    select * from raw.cheddr_weddr.weather_forecast

),

final as (
    select 
        payload:daily_units::variant as daily_units

    from src

)

select * from final