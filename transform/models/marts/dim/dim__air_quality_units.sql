with

src as (

    select top 1
        hourly_units
        
    from {{ ref("stg__air_quality")}}

),

flattened as (

    select
        j.key::varchar as field,
        j.value::varchar as units

    from src,
        lateral flatten (input => hourly_units) j

)

select * from flattened