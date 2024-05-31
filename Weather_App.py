

import requests


def get_weather(api_key, location):
    # Construct the URL for the API request
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the response text
        data = response.text
        
        # Find and extract the temperature
        temp_index = data.find('"temp":') + len('"temp":')
        temp_end_index = data.find(',', temp_index)
        temperature = data[temp_index:temp_end_index]
        
        # Find and extract the humidity
        humidity_index = data.find('"humidity":') + len('"humidity":')
        humidity_end_index = data.find(',', humidity_index)
        humidity = data[humidity_index:humidity_end_index]
        
        # Find and extract the weather condition description
        description_index = data.find('"description":"') + len('"description":"')
        description_end_index = data.find('"', description_index)
        description = data[description_index:description_end_index]
        
        # Find and extract the city name
        city_index = data.find('"name":"') + len('"name":"')
        city_end_index = data.find('"', city_index)
        city = data[city_index:city_end_index]
        
        # Print the weather report
        print(f'Weather in {city}:')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Conditions: {description}')
    else:
        print('Failed to retrieve weather data.')

# Replace with your own API key
api_key = '690bf7a0da210094f90f866504c82865'

# Replace with your own location
location = input("enter city:")

get_weather(api_key, location)