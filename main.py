import json
import requests
import apikey

appid = apikey.openweatherapi
city_id = 0


def weatherapp(text):
    place_query = ""
    place_query = text
    place_apikey = apikey.google_place_api

    lat = "lat"
    lon = "lot"

    try:
        place_res = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json',
                                 params={'query': place_query, 'language': 'ru', 'key': place_apikey})
        place_data = place_res.json()

        lon = json.dumps(place_data['results'][0]['geometry']['location']['lng'])
        lat = json.dumps(place_data['results'][0]['geometry']['location']['lat'])
        name = place_data['results'][0]['name']
        print(place_data)

    except Exception as e:
        print("Error requests: ", e)
    pass

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'lat': lat, 'lon': lon, 'units': 'metric',
                                   'lang': 'ru', 'appid': appid})
        data = res.json()
        print(data)

        conditions = data['weather'][0]['description']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        icon = "http://openweathermap.org/img/w/" + str(data['weather'][0]['icon']) + ".png"

        if (temp > 0):
            temp = "+" + str(temp)
        if (temp_min > 0):
            temp_min = "+" + str(temp_min)

        if (temp_max > 0):
            temp_max = "+" + str(temp_max)
        weather=""
        weather = "Сегодня в  <b>" + google_place_api.name + "<b>\n" + "<a href = " + icon + "</a>" + str(
            temp) + "\n" + str(conditions).capitalize() + " от " + str(temp_min) + " до " + str(temp_max)
        return weather
    except Exception as e:
        print(e)
        pass
