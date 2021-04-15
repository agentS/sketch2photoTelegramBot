from telegram import Update
from telegram.ext import CallbackContext

def show_help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Hi, I am a Telegram bot for creating a photo from a sketch and vice versa. If you want to generate a photo from a sketch, just send /sketch2photo and I will assist you. Same thing if you want to generate a sketch from a photo; just text me /photo2sketch and I will do that for you. Thanks for using this bot! :-)'
    )

def show_start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Hi, I am a Telegram bot for creating a photo from a sketch and vice versa.'
    )

def say_hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
