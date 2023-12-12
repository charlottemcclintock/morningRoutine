import requests

def get_sunrise_sunset(lat, lon, date="today"):
    base_url = "https://api.sunrise-sunset.org/json"

    params = {
        "lat": lat,
        "lng": lon,
        "date": date,
        "formatted":1,
        "tzId": "America/Vancouver"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        sunrise = data["results"]["sunrise"]
        sunset = data["results"]["sunset"]
        return sunrise, sunset
    else:
        return None, None

latitude = 47.6061  
longitude = -122.3328  # Seattle

print(get_sunrise_sunset(latitude, longitude))

