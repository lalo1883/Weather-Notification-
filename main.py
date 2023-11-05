import requests
from telegram import Bot
import asyncio

# OpenWeatherMap API key and location details
TOKEN_TELEGRAM = 'YOUR TELEGRAM TOKEN'
API_key = 'YOUR API KEY FOR OPEN WEATHER'
lat = 28.485447
lon = -105.782066
exclude = 'current,minutely,daily'

# Fetch weather data from OpenWeatherMap API
response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_key}')
response.raise_for_status()
weather_data = response.json()['hourly']

# Calculate average temperature for the next 12 hours
hourly_temperatures = []
temps = 0
for i in range(10, 22):
    temp = weather_data[i]['temp'] - 273.15
    temp = round(temp, 2)
    temps += temp / 12
    hour = i - 4
    if temp <= 14:
        message = f'Time {hour}:00.🥶:\ntemperature will be: {temp} C°.\n-----------------------'
    elif temp >= 15:
        message = f'Time {hour}:00.🥵:\ntemperature will be: {temp} C°.\n-----------------------'
    hourly_temperatures.append(message)

final_message = '\n'.join(hourly_temperatures)

# Send weather updates to Telegram chat
async def send_message():
    bot = Bot(token=TOKEN_TELEGRAM)
    await bot.sendMessage(chat_id=YOUR_CHAT_ID, text=final_message)

# Determine and send cold or hot weather message based on average temperature
async def total_temp():
    bot = Bot(token=TOKEN_TELEGRAM)
    round(temps, 2)
    cold_message = f'The average temperature is going to be: {temps}. 🥶'
    heat_message = f'The average temperature is going to be: {temps}. 🥵'
    if temps >= 15:
        await bot.sendMessage(chat_id=YOUR_CHAT_ID, text=heat_message)
    elif temps <= 14:
        await bot.sendMessage(chat_id=YOUR_CHAT_ID, text=cold_message)

# Run the functions
asyncio.run(send_message())
asyncio.run(total_temp())
