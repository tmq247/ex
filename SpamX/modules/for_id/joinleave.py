
# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!



from .. import (handler, Sudos, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX import join_errors, leave_errors


@Client.on_message(filters.user(Sudos) & filters.command(["join"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["join"], prefixes=handler))
async def join(SpamX: Client, e: Message):
    chat = e.text[6:]
    if chat.isnumeric():
        return await e.reply_text("Không thể tham gia trò chuyện với id trò chuyện. Cung cấp tên người dùng hoặc liên kết mời.")
    try:
      await SpamX.join_chat(chat)
      await e.reply_text("**Tham gia thành công ✅ **")
    except Exception as ex:
      await e.reply_text(join_errors(ex))
    if LOGS_CHANNEL:
         try:
             await SpamX.send_message(LOGS_CHANNEL, f"Đã tham gia cuộc trò chuyện mới \n\n Trò chuyện: {chat} \n Cmd theo người dùng: {e.from_user.id}")
         except Exception as a:
             print(a)
             pass

@Client.on_message(filters.user(Sudos) & filters.command(["leave"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["leave"], prefixes=handler))
async def leave(SpamX: Client, e: Message):
    rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        chat = rizoel[0]
        try:
           if chat in [-1002025317318, 6337933296, "@coihaycoc"]:
              return
           await SpamX.leave_chat(chat)
           await e.reply_text("**Rời đi thành công ✅ **")
        except Exception as ex:
           await e.reply_text(leave_errors(ex))
    else:
        chat = e.chat.id
        ok = e.from_user.id
        if int(chat) == int(ok):
            return await e.reply_text(f"Cách sử dụng: {handler}leave <tên người dùng hoặc id trò chuyện> or {handler}leave (nhập trực tiếp trong Nhóm muốn rời khỏi)")
        if int(chat) == -1002025317318:
              return
        try:
           await SpamX.leave_chat(chat)
           await e.reply_text("**Rời đi thành công ✅ **")
        except Exception as ex:
           await e.reply_text(leave_errors(ex))
        if LOGS_CHANNEL:
           try:
                await SpamX.send_message(LOGS_CHANNEL, f"Đã rời khỏi cuộc trò chuyện \n\n Trò chuyện: {chat} \n Cmd theo người dùng: {e.from_user.id}")
           except Exception as a:
             print(a)
             pass
