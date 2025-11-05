with 

src as (
    select * from {{ source('cheddr_weddr', 'weather_forecast') }}

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
