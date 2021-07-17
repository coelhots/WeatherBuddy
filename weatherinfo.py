import requests
from flask import Flask, request, json

app = Flask(__name__)
app.config['DEBUG'] = True
API_KEY = '3b82fc89586f7c60405de9352a0c84eb'

@app.route('/weather', methods=['GET', 'POST'])
def index():
    city_name = request.args.get('city')
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+API_KEY)
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = int(temp_k - 273.15)
    name = (json_object['name'])
    country = (json_object['sys']['country'])
    temp_desc = (json_object['weather'][0]['description'])

    response = {
        "temp_c": temp_c,
        "temp_desc": temp_desc,
        "city" : name,
        "country" : country,
        }
        
    return json.dumps(response)

if __name__ == '__main__':
    app.run(debug=True)