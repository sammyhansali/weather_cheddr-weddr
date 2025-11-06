import sys
import json
import requests
import pathlib
from pprint import pp
import datetime




def make_request(location):

    location_id = location["location_id"]
    latitude = location["latitude"]
    longitude = location["longitude"]
    today = datetime.date.today().strftime('%m%d%Y')

    url = "https://satellite-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": "America/New_York",
        "hourly": [
            "shortwave_radiation", 
            "diffuse_radiation", 
            "direct_radiation", 
            "direct_normal_irradiance", 
            "global_tilted_irradiance", 
            "terrestrial_radiation"
        ],
        "models": "satellite_radiation_seamless",
    }

    try:
        resp = requests.get(url=url, params=params)
        resp.raise_for_status
        if resp.status_code != 200: 
            raise requests.exceptions.HTTPError
        content = json.loads(resp.content)
        fp = pathlib.Path(f"/test_data/{location_id}_{today}__satellite_radiation.json")
        with open(fp, "w") as f:
            json.dump(content, f)

    except requests.exceptions.HTTPError as err:
        print("API request failed. Error details: ", err)

    except Exception as err:
        print("An error occurred. Error details: ", err)