"Dedicating this code to ma luv" # i llost her shes ma MJ https://t.me/WONKRU_HERE/971
"Completely Owned by Roshan-Here"
"Copying Code may violate terms & Conditions, Do Fork & Edit"
"Thanks to Wbb for idea"

from pyrogram import Client
from Python_ARQ import ARQ as ASQ
from asyncio import (gather, sleep, get_event_loop)
from pyrogram import filters, idle
from aiohttp import ClientSession as AskSession
from Config import *

print("First Stage of Ask-me Bot")
Ask = Client(
    "MJ",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=30,
    )
print("INITIALIZING ...")
arq = None #Initialy Empty
BASE_URL = "https://arq.hamker.in" #latest May Varies

async def ASKME(question: str):
    resp = (await arq.asq(question)).result #fetching data
    return  (resp)


async def Ask_reply_msg(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    question = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(ASKME(question), sleep(2)) #Wait to get responce
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, "cancel")

    
@Ask.on_message(filters.private & filters.text & ~filters.command("start") & ~filters.edited & ~filters.group)
async def chat(_, message):
    await Ask_reply_msg(message)

    
@Ask.on_message(filters.command("start") & ~filters.edited & ~filters.group)
async def startit(_, message):
    await message.reply_text(text=STARTEXT, reply_markup=BUTTON)
    
# Will add Group-Mode Sooon :) i'm bcy 

print("Starting ASk-me Bot")
async def main():
    global arq
    asksession = AskSession()
    arq = ASQ(BASE_URL, ARQ, asksession) #latest
    await Ask.start()
    print(
      """
          ---------------------------------
           Explore & Enjoy With your Doubts
          ---------------------------------
      """)
    await idle()


loop = get_event_loop() #to check initial stage If not Create New 
loop.run_until_complete(main())
