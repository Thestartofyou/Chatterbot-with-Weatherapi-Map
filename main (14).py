from chatterbot import ChatBot
import requests
import time

# Create a new chatbot
bot = ChatBot('WeatherBot')

# Set up API credentials
api_key = 'your_api_key_here'
city_name = 'New York'  # Replace with your desired city

# Define a function to get the weather data from the API
def get_weather():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

# Define a function to format the weather data into a message
def format_message(data):
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    return f"The current temperature in {city_name} is {temp}°C with {desc}."

# Define a function to have the chatbot speak the weather message
def say_weather():
    data = get_weather()
    message = format_message(data)
    bot_response = bot.get_response(message)
    print(bot_response)

# Set up a loop to check the weather every hour
while True:
    say_weather()
    time.sleep(3600)  # Wait for an hour before checking again

