def weather():
    return {
        "url": "https://api.open-meteo.com/v1/forecast",
        "params": {
            "forecast_days": 1,
            "temperature_unit": "fahrenheit",
            "timezone": "America/New_York",
            "hourly": [
                "temperature_2m",
                "relative_humidity_2m",
                "dew_point_2m",
                "apparent_temperature",
                "precipitation_probability",
                "precipitation",
                "rain",
                "showers",
                "snowfall",
                "snow_depth",
                "wind_speed_10m",
                "weather_code",
                "visibility",
                "wind_direction_10m",
                "wind_gusts_10m",
                "cloud_cover",
                "et0_fao_evapotranspiration",
            ],
        }
    }
    # return url, params

def air_quality():
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "forecast_days": 1,
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
    return url, params

def satellite_radiation():
    url = "https://satellite-api.open-meteo.com/v1/archive"
    params = {
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
    return url, params

def flood():
    url = "https://flood-api.open-meteo.com/v1/flood"
    params = {
        "forecast_days": 1,
        "timezone": "America/New_York",
        "daily": "river_discharge",
    }

    return url, params
