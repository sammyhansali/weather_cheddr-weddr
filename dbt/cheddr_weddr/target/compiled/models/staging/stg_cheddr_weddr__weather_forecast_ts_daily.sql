with 

src as (
    select * from raw.cheddr_weddr.weather_forecast

),

final as (
    select 
        payload:daily::variant as daily

    from src

)

select * from final