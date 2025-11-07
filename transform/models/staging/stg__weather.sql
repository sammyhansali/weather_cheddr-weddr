with

src as (

    select
        location_id,
        date,
        load_ts,
        payload:hourly as hourly
        
    from {{ source('cheddr_weddr', 'weather')}}

),

ts_times_1 as (

    select distinct
        j.value::datetime as ts_time
    
    from src,
        lateral flatten(input => hourly:time) j

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
        f.date,
        f.load_ts

    from src as f,
        lateral flatten (input => hourly) j,
            lateral flatten (input => j.value) k
    join ts_times_2 as tt
        on tt.ts_index = k.index
    where field <> 'time'

)

select * from flattened