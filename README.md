# Data definitions

- RAW: weather api data directly ingested into snowflake
- SRC: raw data that was processed from json to a real table
- STG: src data with modifications and materialized as view
- INT: (optional) acts as intermediate between stg views and marts tables
- MARTS
    - FCT - fact table
    - DIM - dimension table