-- create databases and schemas
create database if not exists RAW;
create database if not exists DEV;
create database if not exists PROD;
create schema if not exists RAW.CHEDDR_WEDDR;
create schema if not exists DEV.CHEDDR_WEDDR;
create schema if not exists PROD.CHEDDR_WEDDR;

-- create warehouses
create warehouse if not exists loading
  warehouse_size = 'xsmall';
create warehouse if not exists transforming
  warehouse_size = 'xsmall';
create warehouse if not exists reporting
  warehouse_size = 'xsmall'; 

-- create roles
create role if not exists loader;
create role if not exists transformer;
create role if not exists reporter;

-- role permissions
-- warehouses
grant usage on warehouse loading      to role loader;
grant usage on warehouse transforming to role transformer;
grant usage on warehouse reporting    to role reporter;

-- databases
grant usage on database RAW to role loader;
grant usage on database DEV to role transformer;
grant usage on database PROD to role transformer;
grant usage on database PROD to role reporter;

grant role loader to user shansali3;
grant role transformer to user shansali3;
grant role reporter to user shansali3;

-- -- RAW: loader builds/owns; transformer only reads
-- grant usage on all schemas    in database RAW to role loader;
-- grant usage on future schemas in database RAW to role loader;
-- grant create schema on database RAW to role loader;  -- if your loaders create connector-specific schemas

-- grant create table, create view, create stage, create file format
--   on all schemas    in database RAW to role loader;
-- grant create table, create view, create stage, create file format
--   on future schemas in database RAW to role loader;

-- grant usage on all schemas    in database DEV to role transformer;
-- grant usage on future schemas in database DEV to role transformer;
-- grant select on all tables     in database DEV to role transformer;
-- grant select on future tables  in database DEV to role transformer;
-- grant select on all views      in database DEV to role transformer;
-- grant select on future views   in database DEV to role transformer;

-- -- PROD: transformer builds/owns; reporter only reads
-- grant usage on all schemas    in database PROD to role transformer;
-- grant usage on future schemas in database PROD to role transformer;
-- grant create schema on database PROD to role transformer;

-- grant create table, create view, create materialized view, create stage
--   on all schemas    in database PROD to role transformer;
-- grant create table, create view, create materialized view, create stage
--   on future schemas in database PROD to role transformer;

-- grant usage on all schemas    in database PROD to role reporter;
-- grant usage on future schemas in database PROD to role reporter;
-- grant select on all tables     in database PROD to role reporter;
-- grant select on future tables  in database PROD to role reporter;
-- grant select on all views      in database PROD to role reporter;
-- grant select on future views   in database PROD to role reporter;