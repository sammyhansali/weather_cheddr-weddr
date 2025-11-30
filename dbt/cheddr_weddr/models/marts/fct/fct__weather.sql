{{
    config(
        materialized='incremental',
        unique_key=["location_id", "ts_time", "field"],
        incremental_strategy="append",  
        on_schema_change="fail"
    )
}}

with

src as (

    select
        location_id,
        data_date,
        load_ts,
        hourly
        
    from {{ ref("stg__weather")}}

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
        f.data_date,
        f.load_ts

    from src as f,
        lateral flatten (input => hourly) j,
            lateral flatten (input => j.value) k
    join ts_times_2 as tt
        on tt.ts_index = k.index
    where field <> 'time'

)

select * from flattened
{% if is_incremental() %}

  -- this filter will only be applied on an incremental run
  -- (uses >= to include records arriving later on the same day as the last run of this model)
  where data_date >= (select coalesce(max(ts_time), '1900-01-01') from {{ this }})

{% endif %}
