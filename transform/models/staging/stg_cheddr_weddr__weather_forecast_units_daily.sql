with 

src as (
    select * from {{ source('cheddr_weddr', 'weather_forecast') }}

),

unload_json as (
    select 
        payload:daily_units::variant as daily_units

    from src

),

final as (
    select 
        j.key as field,
        j.value::varchar as units
        
    from unload_json,
        lateral flatten (input => daily_units) j
)

select * from final