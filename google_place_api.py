import requests
import json
import apikey

place_apikey = apikey.google_place_api
place_query = ""
lat = 0
lon = 0

try:
    place_res = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json',
                             params={'query': place_query, 'language': 'ru', 'key': place_apikey})
    place_data = place_res.json()

    lon = json.dumps(place_data['results'][0]['geometry']['location']['lng'])
    lat = json.dumps(place_data['results'][0]['geometry']['location']['lat'])
    name = place_data['results'][0]['name']

#print(place_data)
# print("\n\nFile google_place_api.py \nLng:"+lon+"\nLat:"+lat+"\nName(google):"+name)
except Exception as e:
print("Error requests: ", e)
pass
