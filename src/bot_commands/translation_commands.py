from telegram import Update
from telegram.ext import CallbackContext

def start_translate_sketch_to_photo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Okay, I am generating a photo from your sketch. Please send me the sketch. Also, please note that I will resize the sketch into a 256x256 RGB file.')

def start_translate_photo_to_sketch(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Cool, let\'s transfrom your photo into a sketch. Please send me the photo. Also, please note that I will resize the photo into a 256x256 RGB file.')
