 -- noqa: Should accept a string instead of a integer
    
    
    
    create table ANALYTICS.CHEDDR_WEDDR.seed_locations (LOCATION_ID bigint,CITY VARCHAR,STATE VARCHAR,COUNTRY VARCHAR,LONGITUDE FLOAT,LATITUDE FLOAT)
  ;
    -- dbt seed --
    
            insert into ANALYTICS.CHEDDR_WEDDR.seed_locations (LOCATION_ID, CITY, STATE, COUNTRY, LONGITUDE, LATITUDE) values
            (%s,%s,%s,%s,%s,%s),(%s,%s,%s,%s,%s,%s),(%s,%s,%s,%s,%s,%s),(%s,%s,%s,%s,%s,%s)
        

;
  