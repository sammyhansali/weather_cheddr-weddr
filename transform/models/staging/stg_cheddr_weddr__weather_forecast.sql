with 

src as (
    select * from {{ source('cheddr_weddr', 'weather_forecast') }}

),

final as (
    select 
        payload:latitude::float as latitude,
        payload:longitude::float as longitude,
        payload:generationtime_ms::time as generationtime_ms,
        payload:utc_offset_seconds::number as utc_offset_seconds,
        payload:timezone::varchar as timezone,
        payload:timezone_abbreviation::varchar as timezone_abbreviation,
        payload:elevation::number as elevation,
        location,
        source,
        current_timestamp() as load_ts

    from src

)

select * from final