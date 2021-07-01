import html
from typing import Optional, List
import re

from telegram import Message, Chat, Update, User, ChatPermissions

from SaitamaRobot import TIGERS, WOLVES, dispatcher
from SaitamaRobot.modules.helper_funcs.chat_status import (
    bot_admin,
    is_user_admin,
    user_admin,
    user_admin_no_reply,
)
from SaitamaRobot.modules.log_channel import loggable
from SaitamaRobot.modules.sql import antiflood_sql as sql
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)
from telegram.utils.helpers import mention_html
from SaitamaRobot.modules.helper_funcs.string_handling import extract_time
from SaitamaRobot.modules.connection import connected
from SaitamaRobot.modules.helper_funcs.alternate import send_message
from SaitamaRobot.modules.sql.approve_sql import is_approved

@pbot.on_message(filters.command("tagall") & ~filters.edited & ~filters.bot)
@admins_only
async def tagall(client, message):
    await message.reply("`Processing.....`")
    sh = get_text(message)
    if not sh:
        sh = "Hai"
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j, parse_mode="html")


__mod_name__ = "Tagall"
__help__ = """
- /tagall : Tag semua orang di grup
"""
