
  
    

create or replace transient table DEV.CHEDDR_WEDDR.dim__locations
    
  (
    location_id number primary key,
    city varchar,
    country varchar,
    longitude float,
    latitude float
    
    )

    
    
    
    as (
    select location_id, city, country, longitude, latitude
    from (
        with

src as (
    
    select 
        location_id::number as location_id,
        city::varchar as city,
        country::varchar as country,
        longitude::float as longitude,
        latitude::float as latitude
    
    from DEV.CHEDDR_WEDDR.seed__locations

)

select * from src
    ) as model_subq
    )
;


  