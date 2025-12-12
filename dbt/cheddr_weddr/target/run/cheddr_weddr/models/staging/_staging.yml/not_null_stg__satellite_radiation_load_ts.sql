
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select load_ts
from DEV.CHEDDR_WEDDR.stg__satellite_radiation
where load_ts is null



  
  
      
    ) dbt_internal_test