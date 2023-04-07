<h1>Weather Telegram Bot</h1>

This is a simple, easy to use, telegram bot that uses the OpenWeatherMap API to retrieve weather data (current weather and temperature in °C) by city.

<h2>Requirements</h2>

In order to use this API, it's required to create an account on the OpenWeatherMap official website and generate an API key.
It's also required to create a Telegram bot with a corresponding API key.
The program should work with Python 3.x versions.

<h2>Instructions</h2>

- Replace values for `openweathermap_api_key` and `telegram_bot_api_key` with your own API keys.
- Open your preferred terminal window.
- Change to the same directory of the `main.py` file.
- Run `python3 main.py`.
- On your telegram bot chat, type `/start` to start the conversation, `/stop` to stop it.
- To search for a city, type `/weather` followed by the city and country code. For example, `/weather Paris FR` will return the weather and temperature for the city of Paris, France.
