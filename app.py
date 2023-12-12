from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/api/sunrise-sunset', methods=['GET'])

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

def sunrise_sunset():
    latitude = 47.6061  
    longitude = -122.3328  # Seattle

    sunrise_time, sunset_time = get_sunrise_sunset(lat = latitude, long = longitude)
    
    if sunrise_time and sunset_time:
        return jsonify({
            "sunrise": sunrise_time,
            "sunset": sunset_time
        })
    else:
        return jsonify({"error": "Unable to fetch sunrise/sunset times"}), 500

if __name__ == '__main__':
    app.run(debug=True)



