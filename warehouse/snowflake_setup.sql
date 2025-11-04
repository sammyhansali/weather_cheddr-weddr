create database if not exists RAW;
create database if not exists ANALYTICS;
create schema if not exists RAW.CHEDDR_WEDDR;
create schema if not exists ANALYTICS.CHEDDR_WEDDR;

create warehouse if not exists LOADING warehouse_size = 'XSMALL';
create warehouse if not exists TRANSFORMING warehouse_size = 'XSMALL';
create warehouse if not exists REPORTING warehouse_size = 'XSMALL'; 

create role if not exists LOADER;
create role if not exists TRANSFORMER;
create role if not exists REPORTER;