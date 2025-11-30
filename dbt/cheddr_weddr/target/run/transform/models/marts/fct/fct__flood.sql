-- back compat for old kwarg name
  
  begin;
    
        
            
                
                
            
                
                
            
                
                
            
        
    

    

    merge into ANALYTICS.CHEDDR_WEDDR.fct__flood as DBT_INTERNAL_DEST
        using ANALYTICS.CHEDDR_WEDDR.fct__flood__dbt_tmp as DBT_INTERNAL_SOURCE
        on (
                    DBT_INTERNAL_SOURCE.location_id = DBT_INTERNAL_DEST.location_id
                ) and (
                    DBT_INTERNAL_SOURCE.ts_time = DBT_INTERNAL_DEST.ts_time
                ) and (
                    DBT_INTERNAL_SOURCE.field = DBT_INTERNAL_DEST.field
                )

    
    when matched then update set
        "LOCATION_ID" = DBT_INTERNAL_SOURCE."LOCATION_ID","TS_TIME" = DBT_INTERNAL_SOURCE."TS_TIME","FIELD" = DBT_INTERNAL_SOURCE."FIELD","VALUE" = DBT_INTERNAL_SOURCE."VALUE","DATA_DATE" = DBT_INTERNAL_SOURCE."DATA_DATE","LOAD_TS" = DBT_INTERNAL_SOURCE."LOAD_TS"
    

    when not matched then insert
        ("LOCATION_ID", "TS_TIME", "FIELD", "VALUE", "DATA_DATE", "LOAD_TS")
    values
        ("LOCATION_ID", "TS_TIME", "FIELD", "VALUE", "DATA_DATE", "LOAD_TS")

;
    commit;