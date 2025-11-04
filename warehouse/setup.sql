-- create warehouse ingest
create database if not exists WEATHER;
create schema if not exists OPEN_METEO;
use schema OPEN_METEO;


-- create raw table
create or replace table RAW_CAMBRIDGE_FORECAST (
    payload     variant,
    source      varchar         default 'open-meteo',
    load_ts     timestamp_ntz   default current_timestamp()
)
;
