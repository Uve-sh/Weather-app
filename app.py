from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

API_KEY = os.getenv('API_KEY', '0b278f6beb9ba56afa4ab989a17b425')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    city = request.args.get('city', 'bharuch')
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "main" in data:
        return render_template('index.html', data=data)
    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
