with

src as (

    select top 1 
        payload:hourly_units as hourly_units 

    from {{ source('cheddr_weddr', 'weather')}}

),

flattened as (

    select
        j.key::varchar as field,
        j.value::varchar as units

    from src,
        lateral flatten (input => hourly_units) j

)

select * from flattened