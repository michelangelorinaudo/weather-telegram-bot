import requests
import json
import sys
import logging
from telegram import Bot
from telegram.ext import Updater, CommandHandler

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
openweathermap_api_key = "YOUR OPENWEATHERMAP API KEY"
telegram_bot_api_key = "YOUR TELEGRAM BOT API KEY"

def welcome(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome to your weather assistant! \nPlease type /weather followed by your city. E.g /weather London")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Please type /weather followed by your city. E.g /weather London")

def get_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={openweathermap_api_key}"
    response = requests.get(url, params={"appid": openweathermap_api_key})
    data = json.loads(response.text)
    coordinates = {"latitude": data[0]["lat"], "longitude": data[0]["lon"]}
    logging.debug(f"Coordinates: {coordinates}")
    return coordinates

def get_weather(update, context):
    args = context.args
    city = ' '.join(args)
    city_coordinates = get_coordinates(city)
    latitude = city_coordinates["latitude"]
    longitude = city_coordinates["longitude"]
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={openweathermap_api_key}"
    response = requests.get(url, params={"appid": openweathermap_api_key})
    data = json.loads(response.text)
    logging.info(f"Request response: {data}")
    weather = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"The weather in {city} is {weather} with a temperature of {temp}°C")

def main():
    updater = Updater(telegram_bot_api_key)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", welcome, pass_args=False))
    dp.add_handler(CommandHandler("help", help, pass_args=False))
    dp.add_handler(CommandHandler("weather", get_weather, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
