# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!



import os
import sys
from random import choice
from .. import Owner, handler
from pyrogram import Client, filters
from pyrogram.types import Message


Media = "resources/Profile.jpg"

@Client.on_message(filters.user(Owner) & filters.command(["setpic"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setpic"], prefixes=handler))
async def setpic(SpamX: Client, e: Message):
     replied = e.reply_to_message
     if (replied and replied.media and (replied.photo or (replied.document and "image" in replied.document.mime_type))):
            await SpamX.download_media(message=replied, file_name=Media)
            await SpamX.set_profile_photo(photo=Media)
            await e.reply_text(f"**Đã thay đổi ảnh hồ sơ thành công** ✅")
            if os.path.exists(Media):
               os.remove(Media)
     else:
         await e.reply_text("Trả lời bất kỳ ảnh nào để thay đổi ảnh hồ sơ")
      
etc_bio = "ᴜsᴇʀ ᴏғ ʀɪᴢᴏᴇʟ x"

@Client.on_message(filters.user(Owner) & filters.command(["setname"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setname"], prefixes=handler))
async def setname(SpamX: Client, e: Message): 
     Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
     if e.reply_to_message:
        name = e.reply_to_message.text.markdown
     elif Rizoel:
        name = str(Rizoel[0])
     else:
        await e.reply_text(f"Sử dụng sai! \n cú pháp: {handler}setname (tên)")
        return
     try:
        await SpamX.update_profile(first_name=name, bio=etc_bio)
        await e.reply_text(f"**Tên hồ sơ đã được thay đổi thành công !!** \n\n **Tên mới:** {name}")
     except Exception as ex:
        await e.reply_text(f"**Lỗi !!** \n\n {ex}")
        print(ex)
     
@Client.on_message(filters.user(Owner) & filters.command(["setbio"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setbio"], prefixes=handler))
async def setbio(SpamX: Client, e: Message):
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
      if e.reply_to_message:
        xd = e.reply_to_message.text.markdown
      elif Rizoel:
        xd = str(Rizoel[0])
      else:
        await e.reply_text(f"Sử dụng sai! \n cú pháp: {handler}setbio (bio)")
        return
      ok = await SpamX.get_me()
      nam = ok.first_name
      nam2 = ok.last_name
      try:
         await SpamX.update_profile(first_name=nam, last_name=nam2, bio=xd)
         await e.reply_text(f"**Tiểu sử hồ sơ đã được thay đổi thành công !** \n\n ** Bio mới**: {xd}")
      except Exception as ex:
         await e.reply_text(f"**Lỗi !!** \n\n {ex}")
         print(ex)
      
