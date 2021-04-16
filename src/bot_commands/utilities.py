from telegram import Update, ChatAction
from telegram.ext import CallbackContext

from functools import wraps

def send_typing_indicator(function):
    """Sends a typing indicator while processing the command passed as function."""

    @wraps(function)
    def command_function(update: Update, context: CallbackContext, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return function(update, context, *args, **kwargs)
    
    return command_function
