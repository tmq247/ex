
import os, sys, asyncio, re
from random import choice
from .. import (handler, Sudos, Owner, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message

from RiZoeLX.data import raids, one_word, R7_ban_codes
from RiZoeLX import Devs, res_grps, res_devs
from RiZoeLX.functions import user_only

unlimited = False 

@Client.on_message(filters.user(Sudos) & filters.command(["uspam"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["uspam"], prefixes=handler))
async def uspam(SpamX: Client, e: Message):
    global unlimited
    unlimited = True
    if int(e.chat.id) in res_grps:
       await e.reply_text("**Lấy làm tiếc !! tôi không thể spam ở đây.**")
       return
    msg = str(e.text[6:]) 
    if not msg:
       await e.reply("Gime Spam message bruh!")
       return
    if re.search(res_devs.lower(), msg.lower()):
       await e.reply("**Xin lỗi !!** Tôi không thể Spam trên chủ sở hữu @coihaycoc")
       return

    try:
       while unlimited == True:
           await SpamX.send_message(e.chat.id, msg)
    except Exception as ex:
           print(ex)
           await e.reply_text(f" Lỗi -! \n\n {ex}")
           
    if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"đã bắt đầu Thư rác không giới hạn theo người dùng: {e.from_user.id} \n\n Trò chuyện: {e.chat.id} \n Tin nhắn rác: {msg}")
         except Exception as a:
             print(a)
             pass



@Client.on_message(filters.user(Sudos) & filters.command(["uraid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["uraid"], prefixes=handler))
async def uraid(SpamX: Client, e: Message):
      global unlimited
      unlimited = True
      user = await user_only(SpamX, e, Owner, Sudos)
      mention = user.mention
      try:
         while unlimited == True:
           raid = choice(raids.raid)
           raid_msg = f"{mention} {reply}"
           await SpamX.send_message(e.chat.id, raid_msg)
      except Exception as f:
           await e.reply_text(f" Error -! \n\n {f}")
           return

      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"đã bắt đầu Đột kích theo người dùng: {e.from_user.id} \n\n Trên người dùng: {mention} \n Trò chuyện: {e.chat.id}")
         except Exception as a:
             print(a)
             pass
           

@Client.on_message(filters.user(Sudos) & filters.command(["abuse", "gali"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["abuse", "gali"], prefixes=handler))
async def abuse(SpamX: Client, e: Message): 
     sex = e.text[7:]
     if sex:
          counts = int(sex)
          if int(e.chat.id) in res_grps:
              return await e.reply_text("**Lấy làm tiếc !! tôi không thể spam ở đây.**")
          for _ in range(counts):
              msg = choice(one_word)
              await SpamX.send_message(e.chat.id, msg)
              await asyncio.sleep(0.2)
     else:
          global unlimited
          unlimited = True
          if int(e.chat.id) in res_grps:
               return await e.reply_text("**Lấy làm tiếc !! tôi không thể spam ở đây.**")
          try:
             while unlimited == True:
                 msg = choice(one_word)
                 await SpamX.send_message(e.chat.id, msg)
          except Exception as ex:
              print(ex)
              await e.reply_text(f" Lỗi -! \n\n {ex}")


@Client.on_message(filters.user(Sudos) & filters.command(["stop"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["stop"], prefixes=handler))
async def stop(_, e: Message):
       global unlimited
       unlimited = False
       await e.reply_text("Đã dừng không giới hạn Spam/Raid/abuse -;")

@Client.on_message(filters.user(Sudos) & filters.command(["echo", "repeat"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["echo", "repeat"], prefixes=handler))
async def echo_(SpamX: Client, message: Message):
    txt = ' '.join(message.command[1:])
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    elif txt:
      msg = str(txt)
    else:
        await message.reply_text(f"**Sử dụng sai!** \n\n Cú pháp: {handler}echo (nhắn tin hoặc trả lời tin nhắn)")
        return

    try:
       await message.delete()
       await SpamX.send_message(message.chat.id, msg)
    except Exception as a:
       await SpamX.send_message(message.chat.id, msg)
       print(str(a))

"""Red7 Report through SpamX"""
@Client.on_message(filters.user(Sudos) & filters.command(["report", "red"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["report", "red"], prefixes=handler))
async def Red7_report(SpamX: Client, message: Message):
   chat = message.chat 
   user = message.from_user

   args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
   txt = args[1:]
   if len(txt) == 2:
      try:
         suser = await SpamX.get_users(args[0])
      except Exception as a:
         await message.reply_text(f"**LỖI:** {a}")
         return
      if int(suser.id) in Devs:
         await y.reply_text("Người dùng là Dev của SpamX!")
         return
      elif int(suser.id) == Owner:
         await message.reply_text("Người dùng là chủ sở hữu của các bot này!")
         return
      else:
         if suser.username:
            report_user = suser.username
         else:
            report_user = suser.id
         reason = str(txt[0])
         if re.search(R7_ban_codes.lower(), reason.lower()):
            report_reason = reason
         else:   
            await message.reply_text("**Lỗi:** Mã lý do sai \n\n [Bấm vào đây.](https://t.me/moimoimusicbot) để có được tất cả các mã lý do!", disable_web_page_preview=True)
            return
         proof = str(txt[1])
         if proof.startswith("https://telegra.ph/file") or proof.startswith("https://telegra.ph"):
            report_proof = str(proof)
         else:
            await message.reply_text("need single telegraph link as a proof!")
            return
      try:
         await SpamX.unblock_user("muoimuoimusicbot")
         Report_message = f"/report {report_user} {report_reason} {report_proof}"
         await SpamX.send_message("muoimuoimusicbot", Report_message)
         await asyncio.sleep(2) 
         async for response in SpamX.get_chat_history("muoimuoimusicbot", 1):
            hm = await SpamX.forward_messages(chat.id, "muoimuoimusicbot", response.id)
            await hm.reply_text(f"{user.mention}! Kiểm tra")
      except Exception as eror:
         await message.reply_text(str(eror))

   else:
       await message.reply_text(f"**Cách sử dụng sai!** \n\n Cú pháp: {handler}report (user) (nguyên mã ([đến đây.](https://t.me/moimoimusicbot)) (single proof telegraph link only)", disable_web_page_preview=True)
