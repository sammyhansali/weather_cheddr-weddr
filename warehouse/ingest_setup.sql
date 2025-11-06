-- use database RAW;
-- use schema CHEDDR_WEDDR;
-- create or replace table WEATHER_FORECAST (
--     payload     variant,
--     location    varchar         default 'cambridge,ma,usa',
--     source      varchar         default 'open-meteo',
--     load_ts     timestamp_ntz   default current_timestamp()
-- )
-- ;
use database RAW;
use schema CHEDDR_WEDDR;
create or replace table HISTORICAL_WEATHER (
    payload     variant,
    location    varchar         default 'cambridge,ma,usa',
    source      varchar         default 'open-meteo',
    load_ts     timestamp_ntz   default current_timestamp()
)
;