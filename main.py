import requests
from telegram import Bot
import asyncio

TOKEN_TELEGRAM = 'YOUR TELEGRAM TOKEN'
will_rain: bool
API_key = 'YOUR API KEY FOR OPEN WEATHER'
lat = 28.485447
lon = -105.782066
exclude = 'current,minutely,daily'


response = requests.get(
    f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={API_key}')
response.raise_for_status()

weather_data = response.json()['hourly']
weather_data2 = response.json()

async def total_temp():
    bot = Bot(token=TOKEN_TELEGRAM)
    round(temps, 2)
    cold_message = f'The avarage temperature is going to be: {temps}. 🥶'
    heat_message = f'The avarage temperature is going to be: {temps}. 🥵'
    if temps >= 15:
        await bot.sendMessage(chat_id=YOUR_CHAT_ID, text=heat_message)
    elif temps <= 14:
        await bot.sendMessage(chat_id=YOUR_CHAT_ID, text=cold_message)

hourly_temperatures = []
temps = 0
temps = round(temps, 2)
for i in range(10,22):
    temp = weather_data[i]['temp'] -273.15
    temp = round(temp, 2)
    temps += temp / 12
    hour = i - 4
    if temp <= 14:
        message = f'Time {hour}:00.🥶:\ntemperature will be: {temp} C°.\n-----------------------'
    elif temp >= 15:
        message = f'Time {hour}:00.🥵:\ntemperature will be: {temp} C°.\n-----------------------'
    hourly_temperatures.append(message)

final_message = '\n'.join(hourly_temperatures)

async def send_message():
    bot = Bot(token=TOKEN_TELEGRAM)
    await bot.sendMessage(chat_id=YOUR_CHAT_ID, text=final_message)

asyncio.run(send_message())
asyncio.run(total_temp())

