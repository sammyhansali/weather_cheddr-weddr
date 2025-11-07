import json
from api_request import weather_forecast, air_quality, satellite_radiation, flood
from warehouse.ingest import ingest_setup, ingest_payload

def main():
    """
    what will the app do when fully orchestrated and built out:

    every day at midnight, for location in locations, it will:
    - fetch forecast data for the next day
        - types of forecast data: (1) weather, (2) air quality, (3) satellite radiation, (4) flood
    - update the respective tables with new data
    - update the BI models

    PK for fact tables: location_id, ts, field
    """

    # # Step 1: Make API request and save payload
    fp = "data/locations.json"
    with open(fp, "r") as f:
        locations = json.load(f)
    
    for location in locations:
        if location["country"] != "US":
            satellite_radiation.make_request(location)
        weather_forecast.make_request(location)
        air_quality.make_request(location)
        flood.make_request(location)

    # Step 2: Data ingestion into snowflake
    ## Run the full_snowflake_setup.sql file first
    # ingest_setup()
    # ingest_payload()

    # Step 3: DBT
    
    

if __name__ == "__main__":
    main()