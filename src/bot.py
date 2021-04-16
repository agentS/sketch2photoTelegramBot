from bot_commands.help_commands import show_help, show_start, say_hello
from bot_commands.translation_commands import start_translate_sketch_to_photo, start_translate_photo_to_sketch, receive_and_translate_sketch, cancel_generation
from bot_commands.conversation_states import BotConversationStates

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters, CallbackContext

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
    generation_conversation_handler = ConversationHandler(
        entry_points = [
            CommandHandler('sketch2photo', start_translate_sketch_to_photo),
            CommandHandler('photo2sketch', start_translate_photo_to_sketch),
        ],
        states={
            BotConversationStates.RECEIVE_SKETCH: [MessageHandler(Filters.photo, receive_and_translate_sketch)],
        },
        fallbacks=[CommandHandler('cancel', cancel_generation)]
    )
    updater.dispatcher.add_handler(generation_conversation_handler)

    updater.start_polling()
    updater.idle()
