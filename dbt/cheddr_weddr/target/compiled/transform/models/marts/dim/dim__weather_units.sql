with

src as (

    select top 1
        hourly_units
        
    from ANALYTICS.CHEDDR_WEDDR.stg__weather

),

flattened as (

    select
        j.key::varchar as field,
        j.value::varchar as units

    from src,
        lateral flatten (input => hourly_units) j

)

select * from flattened