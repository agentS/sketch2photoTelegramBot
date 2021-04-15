from help_commands import show_help, show_start, say_hello

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import os
from os.path import join, dirname
from dotenv import load_dotenv

if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)
    del dotenv_path

    updater = Updater(os.getenv('TELEGRAM_BOT_TOKEN'))

    updater.dispatcher.add_handler(CommandHandler('start', show_start))
    updater.dispatcher.add_handler(CommandHandler('help', show_help))
    updater.dispatcher.add_handler(CommandHandler('hello', say_hello))

    updater.start_polling()
    updater.idle()
