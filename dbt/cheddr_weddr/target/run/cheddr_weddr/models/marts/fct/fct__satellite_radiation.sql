begin;
    insert into DEV.CHEDDR_WEDDR.fct__satellite_radiation ("LOCATION_ID", "TS_TIME", "FIELD", "VALUE", "DATA_DATE", "LOAD_TS")
    (
        select "LOCATION_ID", "TS_TIME", "FIELD", "VALUE", "DATA_DATE", "LOAD_TS"
        from DEV.CHEDDR_WEDDR.fct__satellite_radiation__dbt_tmp
    )

;
    commit;