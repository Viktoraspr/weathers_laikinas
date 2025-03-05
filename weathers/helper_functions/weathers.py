import requests

# Vilnius
latitute = 54.68
longitute = 25.27

url = 'https://api.open-meteo.com/v1/forecast?latitude=54.41&longitude=25.16&current=temperature_2m'

new_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitute}&longitude={longitute}&current=temperature_2m'

print(new_url)

data = requests.get(url=url)

json_data = data.json()

print(json_data['current']['temperature_2m'])


def get_temperature(latitute: float, longitute:float) -> float:
    # ...
    return latitute+longitute
