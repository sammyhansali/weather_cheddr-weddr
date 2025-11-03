-- create warehouse ingest
create database if not exists WEATHER;
create schema if not exists OPEN_METEO;
use schema OPEN_METEO;


-- create staging table
create table if not exists raw_forecast_ ()
