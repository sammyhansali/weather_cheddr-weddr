with

src as (

    select top 1
        daily_units
        
    from {{ ref("stg__flood")}}

),

flattened as (

    select
        j.key::varchar as field,
        j.value::varchar as units

    from src,
        lateral flatten (input => daily_units) j

)

select * from flattened