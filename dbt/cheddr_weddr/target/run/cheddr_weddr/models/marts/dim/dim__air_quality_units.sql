
  
    

create or replace transient table DEV.CHEDDR_WEDDR.dim__air_quality_units
    
  (
    field varchar primary key,
    units varchar
    
    )

    
    
    
    as (
    select field, units
    from (
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
    ) as model_subq
    )
;


  