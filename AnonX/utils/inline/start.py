from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ•",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍂ᴄᴏᴍᴍᴀɴᴅs🍂", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="🥀 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🥀", user_id"5004802508" 
            )
        ],
        [
            InlineKeyboardButton(
                text="💔sᴜᴩᴩᴏʀᴛ💔", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="✨ ᴍʏ ғᴇᴇʟɪɴɢs ✨", url=f"https://instagram.com/official_khan_danish21?igshid=ZDdkNTZiNTM="
            )
        ],
     ]
    return buttons
