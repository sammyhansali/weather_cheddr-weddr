
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select hourly
from ANALYTICS.CHEDDR_WEDDR.stg__weather
where hourly is null



  
  
      
    ) dbt_internal_test