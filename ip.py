import requests
data = requests.get('https://api.ipdata.co?api-key=test').json()
lat = data['latitude']
lon = data['longitude']
print(lat, lon)