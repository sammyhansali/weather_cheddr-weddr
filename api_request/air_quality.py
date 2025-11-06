from api_request.api_request import request_and_save_data

def make_request(location):

    latitude = location["latitude"]
    longitude = location["longitude"]
    location_id = location["location_id"]
    endpoint = "air_quality"

    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "forecast_days": 1,
        "latitude": latitude,
        "longitude": longitude,
        "timezone": "America/New_York",
        "hourly": [
            "pm10", 
            "pm2_5", 
            "carbon_monoxide", 
            "carbon_dioxide", 
            "nitrogen_dioxide", 
            "sulphur_dioxide", 
            "ozone", 
            "aerosol_optical_depth", 
            "dust", 
            "uv_index", 
            "uv_index_clear_sky", 
            "methane",
        ],
    }

    request_and_save_data(url, params, location_id, endpoint)