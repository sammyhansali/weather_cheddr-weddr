from api_request.api_request import request_and_save_data

def make_request(location):

    latitude = location["latitude"]
    longitude = location["longitude"]
    location_id = location["location_id"]
    endpoint = "satellite_radiation"

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

    request_and_save_data(url, params, location_id, endpoint)