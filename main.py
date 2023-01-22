import requests
import json
from telegram import Bot
from telegram.ext import Updater, CommandHandler

def welcome(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Welcome to your weather assistant! \nPlease type /weather followed by your city. E.g /weather London")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Please type /weather followed by your city. E.g /weather London")

def get_weather(update, context):
    args = context.args
    city = ' '.join(args)
    api_key = 'OPENWEATHERMAP API KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    print(response)
    data = json.loads(response.text)
    print(data)
    weather = data['weather'][0]['description']
    temp = data['main']['temp'] - 273.15
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'The weather in {city} is {weather} with a temperature of {temp}°C')

def main():
    updater = Updater('TELEGRAM BOT API KEY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', welcome, pass_args=False))
    dp.add_handler(CommandHandler('help', help, pass_args=False))
    dp.add_handler(CommandHandler('weather', get_weather, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
