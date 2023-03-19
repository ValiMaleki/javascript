import requests

# API key for OpenWeather API
api_key = "9f95d8a86cee503ea0df7c0d206b8a85"

# Ask user for city name
city = input("Enter city name: ")

# API endpoint URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Send API request
response = requests.get(url)

# Parse JSON response
data = response.json()

# Extract temperature in Kelvin
temp_kelvin = data["main"]["temp"]

# Convert Kelvin to Celsius
temp_celsius = temp_kelvin - 273.15

# Extract weather description
description = data["weather"][0]["description"]

# Print temperature and weather description
print(f"Temperature: {temp_celsius:.1f}°C")
print(f"Weather: {description}")
