# Welcome to Weather Buddy API!

  

  

This project was bootstrapped with [Flask](https://flask.palletsprojects.com/en/2.0.x/).

  

  

This is a simple project made for a technical test using [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/2.0.x/)

  

  

The objective of this test is design and build an application that for a given city name, collects data from the [Open Weather API](https://openweathermap.org/),caches it for some configurable time and returns it as a JSON object. Also returns a configurable number of last searched cities. Using [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/en/2.0.x/) and cosume data from [Open Weather API](https://openweathermap.org/). The test was uploaded to [GitHub](https://github.com/coelhots/WeatherBuddy).

  

  

## Links

  

[Weather Buddy API on GitHub](https://github.com/coelhots/WeatherBuddy)

  

[Weather Buddy Front-end on GitHub](https://github.com/coelhots/WeatherBuddyReact)

  

## Available Scripts

  

  

In the project directory, you can run:

  

  

### Local

  

  

#### `python3 weatherinfo.py`

  

Runs the app in the development mode.

### Endpoints


#### To get cache data for the specified city


Open http://localhost:5000/weather?city="city_name" to get the cache data for the specified city_name, otherwise fetches from the Open Weather API, caches and returns the results.

Exemple: http://localhost:5000/weather?city=Florianopolis

```yaml
  {
  "city": "Florianópolis",
  "country": "BR",
  "icon_url": "http://openweathermap.org/img/wn/01d.png",
  "temp_c": 17,
  "temp_desc": "clear sky"
  }
  ```



#### To cached cities
Open http://localhost:5000/weather?max="number"  to get all the cached cities data, up to the latest n entries (configurable) or max_number (if specified).

Exemple: http://localhost:5000/weather?max=2

```yaml
{
  "0": {
    "base": "stations",
    "clouds": {
      "all": 22
    },
    "cod": 200,
    "coord": {
      "lat": 51.5085,
      "lon": -0.1257
    },
    "dt": 1626880904,
    "id": 2643743,
    "main": {
      "feels_like": 303.66,
      "humidity": 50,
      "pressure": 1023,
      "temp": 302.78,
      "temp_max": 304.89,
      "temp_min": 300.07
    },
    "name": "London",
    "sys": {
      "country": "GB",
      "id": 268730,
      "sunrise": 1626840510,
      "sunset": 1626897898,
      "type": 2
    },
    "timezone": 3600,
    "visibility": 10000,
    "weather": [
      {
        "description": "few clouds",
        "icon": "02d",
        "id": 801,
        "main": "Clouds"
      }
    ],
    "wind": {
      "deg": 90,
      "speed": 4.63
    }
  },
  "1": {
    "base": "stations",
    "clouds": {
      "all": 75
    },
    "cod": 200,
    "coord": {
      "lat": -8.0539,
      "lon": -34.8811
    },
    "dt": 1626881554,
    "id": 3390760,
    "main": {
      "feels_like": 298.63,
      "humidity": 73,
      "pressure": 1019,
      "temp": 298.17,
      "temp_max": 298.17,
      "temp_min": 298.17
    },
    "name": "Recife",
    "sys": {
      "country": "BR",
      "id": 8426,
      "sunrise": 1626856455,
      "sunset": 1626898636,
      "type": 1
    },
    "timezone": -10800,
    "visibility": 10000,
    "weather": [
      {
        "description": "broken clouds",
        "icon": "04d",
        "id": 803,
        "main": "Clouds"
      }
    ],
    "wind": {
      "deg": 120,
      "gust": 12.86,
      "speed": 7.72
    }
  },
```