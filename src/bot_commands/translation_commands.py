from bot_commands.conversation_states import BotConversationStates
from bot_commands.utilities import send_typing_indicator

from telegram import Update
from telegram.ext import CallbackContext

# from PIL import Image

# import io

def start_translate_sketch_to_photo(update: Update, context: CallbackContext) -> BotConversationStates:
    update.message.reply_text('Okay, I am generating a photo from your sketch. Please send me the sketch. Also, please note that I will resize the sketch into a 256x256 RGB file. If you want to cancel this action, just send the command /cancel.')
    return BotConversationStates.RECEIVE_SKETCH

@send_typing_indicator
def receive_and_translate_sketch(update: Update, context: CallbackContext) -> BotConversationStates:
    update.message.reply_text('Nice, I am now generating a photo from the sketch you sent me.')
    photo_byte_array = load_image_from_message(update)
    # photo = Image.open(io.BytesIO(photo_byte_array))
    # photo.show()

    return BotConversationStates.SUCCESS

def load_image_from_message(update: Update) -> bytes:
    photo_file = update.message.photo[-1].get_file()
    photo_byte_array = photo_file.download_as_bytearray()
    return photo_byte_array

def start_translate_photo_to_sketch(update: Update, context: CallbackContext) -> BotConversationStates:
    update.message.reply_text('Cool, let\'s transfrom your photo into a sketch. Please send me the photo. Also, please note that I will resize the photo into a 256x256 RGB file. In case you want to cancel this action, send me the command /cancel.')
    return BotConversationStates.RECEIVE_PHOTO

def cancel_generation(update: Update, context: CallbackContext) -> BotConversationStates:
    update.message.reply_text('No problem, I will cancel this generation job.')
    return BotConversationStates.END
