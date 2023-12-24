

import os
import asyncio
from .. import handler, Owner
from pyrogram import Client, filters
from pyrogram.types import Message

from RiZoeLX import Devs, res_grps

@Client.on_message(filters.user(Devs) & filters.command(["msgall"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["msgall"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["msgall"], prefixes=handler))
async def msgall(SpamX: Client, message: Message): 
    txt = ' '.join(message.command[1:])
    if txt:
       msg = str(txt)
    elif message.reply_to_message:
       msg = message.reply_to_message.text.markdown
    else:
       await message.reply_text("Gửi tin nhắn!")
       return
    chat = message.chat
    user = message.from_user
    if chat.id == user.ud:
       """ Không thể sử dụng Cmd này trong PM """
       await message.reply_text("Sử dụng Cmd này trong nhóm")
       return
    if int(chat.id) in res_grps:
       await message.reply_text("**Lấy làm tiếc !! Bạn không thể sử dụng cmd này trong Nhóm này-!**")
       return
    Sah = await message.reply_text("__Gửi tin nhắn cho tất cả thành viên nhóm__")
    done = 0
    fail = 0
    async for x in SpamX.get_chat_members(chat):
       chat_user = x.user
       try:
          await SpamX.send_message(chat_user.id, msg)
          done += 1
          await asyncio.sleep(3)
       except Exception as a:
          fail += 1
          print(a)
    await SpamX.send_message(user.id, f"Đã nhắn tin cho tất cả thành viên trong nhóm! \n\ngửi đến `{done}` users \nthất bại: `{fail}`")
    await sab.delete()
