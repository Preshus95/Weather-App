from flask import Flask, request, jsonify, render_template
from weather import get_curent_weather
from waitress import serve
import os, requests

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    weather_data = get_curent_weather(city)
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)