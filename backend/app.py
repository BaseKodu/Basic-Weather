# app.py
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

WEATHER_API_KEY = 'e636b935e7bd22ac31a519d5fde8202e'
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'


@app.route('/')
def index():
    return render_template('index.html')


# ... other routes and code


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }

    response = requests.get(WEATHER_API_URL, params=params)
    data = response.json()

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
