"""
Maintain, Telegram Maintain Bot

Copyright (C) 2021 Vivek-TP <https://t.me/Vivek_Kerala>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
    "Maintain-Bot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

updatesc = os.environ["UPDATES_CHANNEL"]
supportc = os.environ["SUPPORT_CHAT"]

BOT_TEXT = """
Hi {}👋,

Thank you for showing interest in my works. 

To support my works, please feel free to donate any amount you like. 

There are multiple ways to donate:
👉 UPI 👉 shalualex123@oksbi
👉 GitHub Sponsors
👉 Google Pay
👉 PhonePe

© Mallu Torent ™
"""


@Bot.on_message(filters.private)
Send_message=await bot.send_photo(
    chat_id = update.chat.id, photo="https://telegra.ph/file/6a4c517182269524e6478.jpg", caption=f"Couldn't Find This Movie.Please Try Again Or Search On Our <b><a href='https://t.me/AVA_updates'>Channel</a></b>. \n\nഈ സിനിമയുടെ ഒറിജിനൽ പേര് ഗൂഗിളിൽ പോയി കണ്ടെത്തി അതുപോലെ ഇവിടെ കൊടുക്കുക 🥺", parse_mode="html",
    reply_to_message_id=update.message_id
    )

print(
    """
Bot Started!!! 
"""
)

Bot.run()
