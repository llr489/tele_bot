from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log')

def greet_user(bot, update):
    text = 'Вызван start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat ID: %s, Message: %s", update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planet(bot, update):
    planets = {
        'mars': ephem.Mars(datetime.datetime.today()),
        'venus': ephem.Venus(datetime.datetime.today()),
        'moon': ephem.Moon(datetime.datetime.today()),
        'sun': ephem.Sun(datetime.datetime.today()),
        'jupiter': ephem.Jupiter(datetime.datetime.today()),
        'saturn': ephem.Saturn(datetime.datetime.today()),
        'mercury': ephem.Mercury(datetime.datetime.today()),
        'neptune': ephem.Neptune(datetime.datetime.today()),
        'uranus': ephem.Uranus(datetime.datetime.today()),
        }
    planet = update.message.text.split()[1].lower()
    if planet in planets:
        constellation = ephem.constellation(planets[planet])
        update.message.reply_text(constellation)
    else:
        update.message.reply_text("Нет такой планеты")


def main():
    mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)

    logging.info('the bot is starting')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
   

    mybot.start_polling()
    mybot.idle()

main()
