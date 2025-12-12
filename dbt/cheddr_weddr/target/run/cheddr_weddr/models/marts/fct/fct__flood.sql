
  
    

create or replace transient table DEV.CHEDDR_WEDDR.fct__flood
    
  (
    location_id number not null references DEV.CHEDDR_WEDDR.dim__locations (location_id),
    ts_time timestamp_ntz not null,
    field varchar not null references DEV.CHEDDR_WEDDR.dim__flood_units (field),
    value float,
    data_date date,
    load_ts timestamp_ntz,
    
    primary key (location_id, ts_time, field)
    )

    
    
    
    as (
    select location_id, ts_time, field, value, data_date, load_ts
    from (
        

with

src as (

    select
        location_id,
        data_date,
        load_ts,
        daily
        
    from DEV.CHEDDR_WEDDR.stg__flood

),

ts_times_1 as (

    select distinct
        j.value::datetime as ts_time
    
    from src,
        lateral flatten(input => daily:time) j

),

ts_times_2 as (

    select 
        (row_number() over (order by ts_time asc) - 1) as ts_index,
        ts_time,

    from ts_times_1

),

flattened as (

    select
        f.location_id,
        tt.ts_time,
        j.key::varchar as field,
        k.value::float as value,
        f.data_date,
        f.load_ts

    from src as f,
        lateral flatten (input => daily) j,
            lateral flatten (input => j.value) k
    join ts_times_2 as tt
        on tt.ts_index = k.index
    where field <> 'time'

)

select * from flattened

    ) as model_subq
    )
;


  