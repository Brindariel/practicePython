import requests

api_key='5f6e14104599b0ae5c990d054ef45a45'

weather_input = input("Enter City :")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={weather_input}&appid={api_key}")

if weather_data.json()['cod'] == '404':
    print('No City Found')
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']

    print(f"The Weather in {weather_input} is: {weather}")
    print(f"The Temperature in {weather_input} is: {temp} f")