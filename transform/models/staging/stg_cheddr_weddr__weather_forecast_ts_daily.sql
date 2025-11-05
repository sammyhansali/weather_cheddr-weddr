with 

src as (
    select * from {{ source('cheddr_weddr', 'weather_forecast') }}

),

unload_json as (
    select 
        payload:daily::variant as daily

    from src

),

ts_times as (
    select
        (row_number() over (order by j.value::datetime asc) - 1) as ts_index,
        j.value::datetime as ts_time
    
    from unload_json as w,
        lateral flatten(input => w.daily:time) j

),

ts_vals as (
    select 
        f.index::number as ts_index,
        j.key as field,
        f.value::varchar as value
        
    from unload_json as w,
        lateral flatten (input => daily) j,
        lateral flatten (input => j.value) f
    where field <> 'time'

),

final as (
    select
        tv.ts_index,
        tt.ts_time,
        tv.field,
        tv.value
    from ts_vals as tv
    left join ts_times as tt
        on tv.ts_index = tt.ts_index

)

select * from final