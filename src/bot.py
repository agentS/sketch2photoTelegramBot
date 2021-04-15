from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import os
from os.path import join, dirname
from dotenv import load_dotenv

def say_hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)
    del dotenv_path

    updater = Updater(os.getenv('TELEGRAM_BOT_TOKEN'))

    updater.dispatcher.add_handler(CommandHandler('hello', say_hello))

    updater.start_polling()
    updater.idle()
