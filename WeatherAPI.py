import requests

# replace YOUR_API_KEY with your own API key from OpenWeatherMap
api_key = "YOUR_API_KEY"
city = input("Enter a city name: ")

# create the API request URL with the city and API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# send the request and store the response
response = requests.get(url)

# parse the JSON data from the response into a Python dictionary
data = response.json()

# print out the weather information for the city
print(f"Weather for {city}:")
print(f"Temperature: {data['main']['temp']} Kelvin")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Wind speed: {data['wind']['speed']} meters/sec")
