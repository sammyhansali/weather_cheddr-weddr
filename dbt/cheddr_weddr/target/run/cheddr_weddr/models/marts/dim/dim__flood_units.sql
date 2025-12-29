
  
    

create or replace transient table DEV.CHEDDR_WEDDR.dim__flood_units
    
  (
    field varchar primary key,
    units varchar
    
    )

    
    
    
    as (
    select field, units
    from (
        with

src as (

    select top 1 daily_units

    from DEV.CHEDDR_WEDDR.stg__flood

),

flattened as (

    select
        j.key::varchar as field,
        j.value::varchar as units

    from src,
        lateral flatten(input => daily_units) as j

)

select * from flattened
    ) as model_subq
    )
;


  