import requests
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True
API_KEY = '3b82fc89586f7c60405de9352a0c84eb'

@app.route('/', methods=['GET', 'POST'])
def index():
    cityName = request.args.get('city')
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityName+'&appid=3b82fc89586f7c60405de9352a0c84eb')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = int(temp_k - 273.15)
    temp_desc = str(json_object['description'])

    return temp_c

if __name__ == '__main__':
    app.run(debug=True)