import os
from os import getenv, environ
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Enter Manually or Follw Instructions
API_ID = int(os.environ.get('API_ID', "")) #API_ID = "Place your Telegram API_ID Value"
API_HASH = os.environ.get('API_HASH', "") #API_HASH = "Place Your Telegram API_HASH Value"
BOT_TOKEN = os.environ.get('BOT_TOKEN', "") #BOT_TOKEN = "Place Your Telegram BOT_TOKEN Value"
ARQ = os.environ.get('ARQ', "") #ARQ ="Place Your ARQ Key From tx.me/ARQRobot"
STARTEXT = """
Hai, i'm **Ask-me Bot**
So, What is Ask-me Right ?
its simple you can ask any question to me
like ask me anything if i know i will give you specific answers like your besties,
Now i'm (Source) at V1 Stage,,,
My Developers are Bcy :( 
So now i Only Work for Private Chats Only
    
#Note Dont play with this Asq a Valid Question/Doubts 
    
#Don't Missunderstand Its not an AI Chatbot :)
    
Have a good day
    """
BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Team Xequist', url="https://t.me/XDgangZ")
        ],
        [
            InlineKeyboardButton('Source :)', url="github.com/Roshan-Here/Ask-me-bot")
        ]
    ]
)

# Extra details
__version__ = 'V1'
__author__ = 'Roshan-here'
