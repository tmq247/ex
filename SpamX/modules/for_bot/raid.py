# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL

import os, sys, asyncio
from random import choice
from .. import (Owner, handler, Sudos, LOGS_CHANNEL, DATABASE_URL)
from pyrogram import Client, filters
from pyrogram.types import Message

from RiZoeLX.data import raid_usage, raids
from RiZoeLX import Devs, res_grps
from RiZoeLX.functions import user_only, start_raid

from SpamX.database import raid_db

@Client.on_message(filters.user(Sudos) & filters.command(["raid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["raid"], prefixes=handler))
async def raid(SpamX: Client, e: Message):
      """ Start Raid """
      usage = raid_usage.raid
      Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Rizoel) == 2:
        counts = int(Rizoel[0])
        if not counts:
          await e.reply_text(f"Gime đột kích Đếm hoặc sử dụng `{handler}.uraid` cho các cuộc đột kích không giới hạn!")
          return
        hm = Rizoel[1]
        if not hm:
          await e.reply_text("bạn cần chỉ định một người dùng! Trả lời bất kỳ người dùng hoặc Gime id/username")
          return
        try:
           user = await SpamX.get_users(Rizoel[1])
        except:
           await e.reply_text("**Lỗi:** Không tìm thấy người dùng!")
           return
      elif e.reply_to_message:
        counts = int(Rizoel[0])
        try:
           user = await SpamX.get_users(e.reply_to_message.from_user.id)
        except:
           user = e.reply_to_message.from_user 
      else:
        await e.reply_text(usage.format(handler))
        return

      if int(user.id) == Owner:
         await e.reply_text("Anh chàng này là chủ sở hữu của những Bot này.")
         return
      if int(user.id) in Sudos:
         if e.from_user.id != Owner:
           await e.reply_text("Anh chàng này là người dùng sudo.")
           return

      await start_raid(SpamX, e, counts, user)

      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"đã bắt đầu Đột kích theo người dùng: {e.from_user.id} \n\n Trên người dùng: {mention} \n Trò chuyện: {e.chat.id} \n Counts: {counts}")
         except Exception as a:
            print(a)
            pass


RUSERs = []

@Client.on_message(filters.user(Sudos) & filters.command(["rraid", "replyraid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["rraid", "replyraid"], prefixes=handler))
async def rraid(SpamX: Client, e: Message):
      global RUSERs
      user = await user_only(SpamX, e, Owner, Sudos)

      if DATABASE_URL:
          check = raid_db.check(user.id)
          if check:
             await e.reply_text("Người dùng đã có trong danh sách Raid!")
             return
          raid_db.add_user(user.id)
      else:
          if int(user.id) in RUSERs:
             await e.reply_text("Người dùng đã có trong danh sách Raid!")
             return
          RUSERs.append(user.id)                
      mention = user.mention
      await e.reply_text(f"Reply Raid Activated On User {mention}")
            
      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f"Kích hoạt trả lời đột kích bởi người dùng: {e.from_user.id} \n\n Trên người dùng: {mention} \n Trò chuyện: {e.chat.id}")
         except Exception as a:
             print(a)
             pass


@Client.on_message(filters.user(Sudos) & filters.command(["draid", "dreplyraid"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["draid", "dreplyraid"], prefixes=handler))
async def draid(SpamX: Client, e: Message):
      global RUSERs
      user = await user_only(SpamX, e, Owner, Sudos)

      if DATABASE_URL:
         check = raid_db.check(user.id)
         if not check:
             await e.reply_text("Người dùng không có trong danh sách Raid!")
             return 
         raid_db.rm_user(user.id)
      else:
         if int(user.id) not in RUSERs:
           await e.reply_text("Người dùng không có trong danh sách Raid!")
           return
         RUSERs.remove(user.id)
      mention = user.mention
      await e.reply_text(f"Trả lời Raid được kích hoạt thành công trên người dùng {mention}")
      
      if LOGS_CHANNEL:
         try:
            await SpamX.send_message(LOGS_CHANNEL, f" Cuộc đột kích trả lời của người dùng đã bị vô hiệu hóa: {e.from_user.id} \n\n Người dùng: {mention} \n Trò chuyện: {e.chat.id}")
         except Exception as a:
             print(a)
             pass

@Client.on_message(filters.all)
async def watcher(_, msg: Message):
    global RUSERs
    if int(msg.chat.id) in res_grps:
       return
    if DATABASE_URL:
       check = raid_db.check(msg.from_user.id)
       if check:
         await msg.reply_text(choice(raids.replyraids))
    else:
       if int(msg.from_user.id) in RUSERs:
         await msg.reply_text(choice(raids.replyraids))       

@Client.on_message(filters.user(Sudos) & filters.command(["rlist", "raidlist"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["rlist", "raidlist"], prefixes=handler))
async def raidlist(SpamX: Client, message: Message):
    global RUSERs
    _reply = "**Danh sách người dùng đột kích - SpamX** \n\n"
    if DATABASE_URL:
       data = raid_db.get_all_raiders()
       if len(data) > 0:
          for x in data:
             try:
                user = await SpamX.get_users(x.user_id)
                _reply += f" × {user.mention} \n"
             except:
                _reply += f" × [{x.user_id}](tg://user?id={x.user_id}) \n"
       else:
          await message.reply_text("Chưa!")
          return
    else:
       if len(RUSERs) > 0:
          for x in RUSERs:
             try:
                user = await SpamX.get_users(x)
                _reply += f" × {user.mention} \n"
             except:
                _reply += f" × [{x}](tg://user?id={x}) \n"
       else:
          await message.reply_text("Chưa!")
          return
    await message.reply_text(_reply)
