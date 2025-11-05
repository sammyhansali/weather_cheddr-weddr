with src as 
(
    select
        *
    from {{ source('cheddr_weddr', 'weather_forecast') }}
)

select * from src