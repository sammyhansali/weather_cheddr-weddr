begin;
    insert into DEV.CHEDDR_WEDDR.fct__air_quality ("LOCATION_ID", "TS_TIME", "FIELD", "VALUE", "DATA_DATE", "LOAD_TS")
    (
        select "LOCATION_ID", "TS_TIME", "FIELD", "VALUE", "DATA_DATE", "LOAD_TS"
        from DEV.CHEDDR_WEDDR.fct__air_quality__dbt_tmp
    )

;
    commit;