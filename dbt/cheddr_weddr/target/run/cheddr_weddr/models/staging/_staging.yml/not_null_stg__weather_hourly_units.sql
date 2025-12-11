
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select hourly_units
from ANALYTICS.CHEDDR_WEDDR.stg__weather
where hourly_units is null



  
  
      
    ) dbt_internal_test