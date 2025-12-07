from sys import api_version
from dotenv import dotenv_values

import requests

def get_weather_data(city_name, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    params = {"q":city_name, "appid": api_key, "units":"metric"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code} - {response.text}")

def display_weather_info(weather_data):
    print(weather_data)
    city = weather_data['name']
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temp} Celcius")
    print(f"Description: {description.capitalize()}")
    print(f"Humidity: {humidity}")
    print(f"Wind Speed: {wind_speed}")

def main():
    # api_key = "6ab142a1d8febfc1d3e08fb8051a6fa9"
    values = dotenv_values(".env")
    api_key = values["APIKEY"]

    while True:
        city_name = input("Enter city name: ").strip()
        while not city_name:
            print("Not found")
            city_name = input("Enter city name: ").strip()
            break

        weather_data = get_weather_data(city_name, api_key)
        if weather_data:
            display_weather_info(weather_data)
            break
        else:
            print("Object not found")

main()