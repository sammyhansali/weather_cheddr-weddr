
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select data_date
from ANALYTICS.CHEDDR_WEDDR.stg__satellite_radiation
where data_date is null



  
  
      
    ) dbt_internal_test