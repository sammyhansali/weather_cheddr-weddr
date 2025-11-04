import os
import pathlib
from api_request.weather_forecast import make_request
from warehouse.ingest import ingest_setup, ingest_payload

def main():
    
    # Step 1: Make API request and save payload
    fp = pathlib.Path("C:/Users/sammy/projects/portfolio/weather_cheddr-weddr/test_data/payload.json")
    if not os.path.exists(fp):
        make_request()

    # Step 2: Data ingestion into snowflake
    ingest_setup()
    ingest_payload()

    # Step 3: DBT
    
    

if __name__ == "__main__":
    main()
