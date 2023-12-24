# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL

import os, sys, asyncio
from random import choice
from .. import (Owner, handler, Sudos, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message

from RiZoeLX.data import dm_usage
from RiZoeLX import Devs
from RiZoeLX.functions import start_dm_spam, start_dm_raid


@Client.on_message(filters.user(Sudos) & filters.command(["dmraid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["dmraid"], prefixes=handler))
async def dmraid(SpamX: Client, message: Message):
      """ Module: Dm Raid """
      usage = dm_usage.dm_raid
      Rizoel = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
        counts = int(Rizoel[0])
        if not counts:
          await message.reply_text("Gime raid Counts")
          return
        hm = Rizoel[1]
        if not hm:
          await message.reply_text("bạn cần chỉ định một người dùng! Trả lời bất kỳ người dùng nào hoặc gime id/username")
          return
        try:
           user = await SpamX.get_users(Rizoel[1])
        except:
           await message.reply_text("**Lỗi:** Không tìm thấy người dùng!")
           return
      elif message.reply_to_message:
        counts = int(Rizoel[0])
        try:
           user = await SpamX.get_users(message.reply_to_message.from_user.id)
        except:
           user = message.reply_to_message.from_user 
      else:
        await message.reply_text(usage.format(handler))
        return

      if int(user.id) == Owner:
         await message.reply_text("Anh chàng này là chủ sở hữu của những Bot này.")
         return
      if int(user.id) in Sudos:
         if message.from_user.id != Owner:
           await message.reply_text("Anh chàng này là người dùng sudo.")
           return
      
      await message.reply_text("🔸 DM Cuộc đột kích bắt đầu 🔸")
      await start_dm_raid(SpamX, message, counts, user.id)
         
      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"DM Đã bắt đầu cuộc tấn công theo người dùng: {message.from_user.mention} \n\n Trên người dùng: {user.id} \n Counts: {counts}")
         except Exception as a:
             print(a)
             pass
         
@Client.on_message(filters.user(Sudos) & filters.command(["dm"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["dm"], prefixes=handler))
async def dm(SpamX: Client, message: Message):
      usage = dm_usage.dm
      Rizoel = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
        hm = Rizoel[0]
        if not hm:
          await message.reply_text("bạn cần chỉ định một người dùng! Trả lời bất kỳ người dùng nào hoặc gime id/username")
          return
        try:
           user = await SpamX.get_users(Rizoel[0])
        except:
           await message.reply_text("**Lỗi:** Không tìm thấy người dùng!")
           return
        dm_msg = str(Rizoel[1])
        if not dm_msg:
           await message.reply_text("Gime Message!")
           return
      elif message.reply_to_message:
        dm_msg = str(Rizoel[1])
        if not dm_msg:
           await message.reply_text("Gime Message!")
        try:
           user = await SpamX.get_users(message.reply_to_message.from_user.id)
        except:
           user = message.reply_to_message.from_user 
      else:
        await message.reply_text(usage.format(handler))
        return

      if int(user.id) == Owner:
         await message.reply_text("Anh chàng này là chủ sở hữu của những Bot này.")
         return
      if int(user.id) in Sudos:
         if message.from_user.id != Owner:
           await message.reply_text("Anh chàng này là người dùng sudo.")
           return

      await SpamX.send_message(user.id, dm_msg)
      await message.reply_text("🔸 Tin nhắn đã gửi 🔸")
      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"Tin nhắn trực tiếp của người dùng: {message.from_user.id} \n\n Trên người dùng: {id}")
         except Exception as a:
             print(a)
             pass

@Client.on_message(filters.user(Sudos) & filters.command(["dmspam"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["dmspam"], prefixes=handler))
async def dmspam(SpamX: Client, message: Message):
      usage = dm_usage.dm_spam
      Rizoel = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
      Rizoelop = Rizoel[1:]
      if len(Rizoelop) == 2:
          msg = str(Rizoelop[1])
          ok = await SpamX.get_users(Rizoel[0])
          id = ok.id
          if int(id) in Devs:
                text = f"Tôi không thể tấn công Chủ sở hữu @coihaycoc"
                await message.reply_text(text)
          elif int(id) == Owner:
                text = f"Anh chàng này là chủ sở hữu của những Bot này."
                await message.reply_text(text)
          elif int(id) in Sudos:
             if message.from_user.id != Owner:
               await message.reply_text("Anh chàng này là người dùng sudo.")
          else:
              counts = int(Rizoelop[0])
              await message.reply_text("☢️ Dm Thư rác đã bắt đầu ☢️")
              await start_dm_spam(SpamX, counts, id, msg)
              
      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          ok = await SpamX.get_users(user_id)
          id = ok.id
          if int(id) == Owner:
                text = f"Anh chàng này là chủ sở hữu của những Bot này."
                await message.reply_text(text)
          elif int(id) in Sudos:
             if message.from_user.id != Owner:
                await message.reply_text("Anh chàng này là người dùng sudo.")
          else:
              counts = int(Rizoel[0])
              msg = str(Rizoelop[0])
              await message.reply_text("☢️ Dm Thư rác đã bắt đầu ☢️")
              await start_dm_spam(SpamX, counts, id, msg)
              
      else:
          await message.reply_text(usage.format(handler))
          return
      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"DM đã bắt đầu Thư rác theo người dùng: {message.from_user.id} \n\n Trên người dùng: {id} \n Counts: {counts} \n Tin nhắn: {msg}")
         except Exception as a:
             print(a)
             pass
