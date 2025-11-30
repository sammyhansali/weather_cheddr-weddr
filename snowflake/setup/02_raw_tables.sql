use database RAW;
use schema CHEDDR_WEDDR;

create or replace table WEATHER (
    payload         variant,
    location_id     varchar         not null,
    date            varchar         not null,
    load_ts         timestamp_ntz   not null
)
;
create or replace table AIR_QUALITY (
    payload         variant,
    location_id     varchar         not null,
    date            varchar         not null,
    load_ts         timestamp_ntz   not null
)
;
create or replace table SATELLITE_RADIATION (
    payload         variant,
    location_id     varchar         not null,
    date            varchar         not null,
    load_ts         timestamp_ntz   not null
)
;
create or replace table FLOOD (
    payload         variant,
    location_id     varchar         not null,
    date            varchar         not null,
    load_ts         timestamp_ntz   not null
)
;