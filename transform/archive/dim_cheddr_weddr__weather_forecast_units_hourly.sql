-- with 

-- stg as (
--     select hourly_units
--     from {{ ref('stg_cheddr_weddr__weather_forecast') }}

-- ),

-- final as (
--     select 
--         j.key as field,
--         j.value::varchar as units
        
--     from stg,
--         lateral flatten (input => hourly_units) j
-- )

-- select * from final
