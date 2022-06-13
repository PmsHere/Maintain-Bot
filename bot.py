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
👉 [GitHub Sponsors](https://github.com/sponsors/PmsHere?o=sd&sc=t)
👉 [Google Pay](https://telegra.ph/file/f1ccbbf3b89c6c45adee8.jpg)
👉 PhonePe 👉 shalu.alex@ybl

© Mallu Torent ™
"""


@Bot.on_message(filters.private)
async def start(bot, update):
    text = BOT_TEXT.format(update.from_user.mention)
    await update.reply_text(
        text=text, disable_web_page_preview=False
    )

print(
    """
Bot Started!!! 
"""
)

Bot.run()
