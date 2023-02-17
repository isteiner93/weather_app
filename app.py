from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = request.args.get('city')

    weather_api_key = '8c947ac7f925522cdd06696d6e6d1a26'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'
    weather_data = requests.get(url).json()

    temperature = weather_data['main']['temp']
    temperature_celsius = round(temperature - 273.15, 2)
    condition = weather_data['weather'][0]['main']
    return render_template('index.html', temperature=temperature_celsius, condition=condition, city=city)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
