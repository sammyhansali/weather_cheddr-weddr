with

src as (

    select top 1 hourly_units

    from DEV.CHEDDR_WEDDR.stg__air_quality

),

flattened as (

    select
        j.key::varchar as field,
        j.value::varchar as units

    from src,
        lateral flatten(input => hourly_units) as j

)

select * from flattened