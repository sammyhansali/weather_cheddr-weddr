with

src as (
    
    select 
        location_id::number as location_id,
        city::varchar as city,
        country::varchar as country,
        longitude::float as longitude,
        latitude::float as latitude
    
    from {{ ref('seed__locations') }}

)

select * from src