-- with 

-- src as (
--     select * from {{ source('cheddr_weddr', 'historical_weather') }}

-- ),

-- final as (
--     select 
--         payload:latitude::float as latitude,
--         payload:longitude::float as longitude,
--         payload:generationtime_ms::time as generationtime_ms,
--         payload:utc_offset_seconds::number as utc_offset_seconds,
--         payload:timezone::varchar as timezone,
--         payload:timezone_abbreviation::varchar as timezone_abbreviation,
--         payload:elevation::number as elevation,
--         payload:hourly::variant as hourly,
--         payload:hourly_units::variant as hourly_units,
--         payload:daily::variant as daily,
--         payload:daily_units::variant as daily_units,
--         location,
--         source,
--         current_timestamp() as load_ts

--     from src

-- )

-- select * from final