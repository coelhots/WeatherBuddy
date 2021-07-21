from typing import Iterator
import requests
import requests_cache
from flask import Flask, request, json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


requests_cache.install_cache('openweather_cache', backend='sqlite', expire_after=300, allowable_methods=('GET', 'POST'))


app.config['DEBUG'] = True
API_KEY = '3b82fc89586f7c60405de9352a0c84eb'



@app.route('/weather', methods=['GET', 'POST'])
def index():

    max = request.args.get('max')

    if max:
        cities_list = {}
        i = 0
        city_cache = requests_cache.patcher.get_cache()
        cities = city_cache.values(True)

        while True:
            try:
                cities_list[i]=next(cities).json()
                i += 1
                if i > int(max) -1:
                    break  

            except StopIteration as e:
                return json.dumps(cities_list)

            
        return json.dumps(cities_list)

    city_name = request.args.get('city')
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+API_KEY)
    json_object = r.json()
    if r.status_code != 200:
        return json_object, 404

    temp_k = float(json_object['main']['temp'])
    
    temp_c = int(temp_k - 273.15)
    name = (json_object['name'])
    icon_url = ('http://openweathermap.org/img/wn/'+json_object['weather'][0]['icon']+'.png')
    country = (json_object['sys']['country'])
    temp_desc = (json_object['weather'][0]['description'])

    response = {
        "temp_c": temp_c,
        "temp_desc": temp_desc,
        "city" : name,
        "country" : country,
        "icon_url": icon_url,
        }
        
    return json.dumps(response)



if __name__ == '__main__':
    app.run(debug=True)