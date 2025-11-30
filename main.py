import json
from api_request import weather, air_quality, satellite_radiation, flood
from ingestion.ingest import ingest_setup, ingest

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

if __name__ == "__main__":
    main()