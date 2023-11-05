Weather Bot using OpenWeatherMap API and Telegram
This Python script fetches hourly weather data for a specific location using the OpenWeatherMap API and sends weather updates to a Telegram chat. It calculates the average temperature for the next 12 hours and sends messages based on whether the average temperature is above or below 15°C.

Prerequisites
Python 3.x
requests library
python-telegram-bot library
Setup Instructions
OpenWeatherMap API Key:

Obtain your OpenWeatherMap API key by signing up on their website: OpenWeatherMap API.
Replace 'YOUR API KEY FOR OPEN WEATHER' with your actual API key in the script.
Telegram Bot Token:

Create a new bot on Telegram and obtain your bot token. You can follow the instructions here: Telegram Bot API.
Replace 'YOUR TELEGRAM TOKEN' with your actual bot token in the script.
Telegram Chat ID:

Replace 'YOUR_CHAT_ID' with the chat ID of the Telegram chat where you want to send weather updates. You can obtain your chat ID by talking to the "Get ID Bot" on Telegram.
How to Run
Run the Python script, and it will fetch the hourly weather data, calculate the average temperature, and send weather updates to the specified Telegram chat.
