"""
     SpamX - Telegram Bots
     © RiZoeLX - 2022-2023
"""
import os, sys, asyncio, datetime, time, subprocess
from .. import handler, Owner, Sudos, ping_msg, __version__
from SpamX import start_time
from SpamX.config import group_welcome

from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.enums import ChatType

from RiZoeLX.data import Variables, Variables_text
from RiZoeLX import Devs
from RiZoeLX.functions import get_time, delete_reply, Red7_Watch as oops_watch


@Client.on_message(filters.user(Sudos) & filters.command(["ping"], prefixes=handler))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      pong_msg = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await pong_msg.edit_text(f"⌾ {ping_msg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")
      
@Client.on_message(filters.me & filters.command(["ping"], prefixes=handler))
async def ping_me(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      try:
        pong_msg = await e.edit_text("**Pong !!**")
      except:
        pong_msg = await e.reply("**Pong !!**")
        await e.delete()    
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await pong_msg.edit_text(f"⌾ {ping_msg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")


@Client.on_message(filters.user(Owner) & filters.command(["getvars", "getvar"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["getvars", "getvar"], prefixes=handler))
async def all_vars(_, message: Message):
    await message.reply_text(f"All Variables given below 👇\n\n {Variables_text} \n\n © @RiZoeLX")

@Client.on_message(filters.user(Owner) & filters.command(["scrape", "inviteall"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["scrape", "inviteall"], prefixes=handler))
async def scrape_members(SpamX: Client, message: Message):
   txt = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
   if message.chat.id == message.from_user.id:
     await message.reply_text("Sử dụng CMD này trong nhóm;")
     return
   if txt:
      xchat = str(txt[0])
      try:
         cht = await SpamX.get_chat(xchat)
         await SpamX.join_chat(cht.username)
      except Exception as a:
         return await message.reply_text(str(a))
      await message.reply_text(f"mời người dùng từ @{cht.username}")
      added = 0
      async for x in SpamX.get_chat_members(cht.id):
        user = x.user
        try:
           await SpamX.add_chat_members(message.chat.id, user.id)
           prini(f"SpamX [THÔNG TIN]: Nhật ký cạo- Thêm {user.id}")
           added += 1
           await asyncio.sleep(2)
        except Exception as a:
           print(f"[SpamX THÔNG TIN]: {str(a)}")
      return await Spamx.send_message(message.chat.id, f"**Người dùng đã thêm!** \nTừ trò chuyện: @{cht.username} \nTổng số người dùng đã thêm: `{added}` \n\n © @coihaycoc")
   else:
      await message.reply_text(f"**Sử dụng sai** \n cú pháp: {handler}scrape @chatlink")

@Client.on_message(filters.user(Sudos) & filters.command(["restart", "reboot"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["restart", "reboot"], prefixes=handler))
async def restarter(SpamX: Client, message: Message):
   await message.reply_text("**Bắt đầu lại...** \n Vui lòng chờ!")
   try:
     await SpamX.stop()
   except Exception as error:
     print(str(error))

   args = [sys.executable, "-m", "SpamX"]
   os.execl(sys.executable, *args)
   quit()

@Client.on_message(filters.user(Sudos) & filters.command(["stats", "stat"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["stats", "stat"], prefixes=handler))
async def stats(SpamX: Client, message: Message):
    tx = await message.reply_text("sưu tập..")
    start = datetime.datetime.now()
    private = 0
    gc = 0
    supergc = 0
    channel = 0
    bot = 0
    admingc = 0
    Me = await SpamX.get_me()
    async for dialog in SpamX.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            private += 1
        elif dialog.chat.type == ChatType.BOT:
            bot += 1
        elif dialog.chat.type == ChatType.GROUP:
            gc += 1
        elif dialog.chat.type == ChatType.SUPERGROUP:
            supergc += 1
            hm = await dialog.chat.get_member(int(Me.id))
            if hm.status in ("creator", "administrator"):
                admingc += 1
        elif dialog.chat.type == ChatType.CHANNEL:
            channel += 1

    end = datetime.datetime.now()
    ms = (end - start).seconds
    stats = f"{Me.first_name}'s stats \n\n"
    stats += "------------- » «» « ------------- \n"
    stats += f"tin nhắn riêng tư: `{private}` \n"
    stats += f"Bot trong Hộp thư đến: `{bot}` \n"
    stats += f"Tổng số nhóm: `{gc}` \n"
    stats += f"Tổng số siêu nhóm: `{supergc}` \n"
    stats += f"Tổng số kênh: `{channel}` \n"
    stats += f"Quản trị viên ở: `{admingc}` cuộc trò chuyện \n\n"
    stats += "------------- » «» « ------------- \n"
    stats += f"Mất thời gian `{ms} giây` \n"
    stats += "© @coihaycoc"
    await delete_reply(message, tx, stats) 

@Client.on_chat_member_updated(filters.group, group=69)
async def welcome_watcher(SpamX: Client, member: ChatMemberUpdated):
   if (
        member.new_chat_member
        and member.new_chat_member.status not in {CMS.BANNED, CMS.LEFT, CMS.RESTRICTED}
        and not member.old_chat_member
   ):
        pass
   else:
        return

   mai = await SpamX.get_me()
   user = member.new_chat_member.user if member.new_chat_member else member.from_user    
   if group_welcome:
      if user.id == mai.id:
         await SpamX.send_message(message.chat.id, "SpamX Here. Powered by @coihaycoc!")
         return
      if user.id == Owner:
         await SpamX.send_message(message.chat.id, f"{user.mention} Welcome to {message.chat.title} my King 👑")
         return
      if user.id in Devs:
         await SpamX.send_message(message.chat.id, f"{user.mention} SpamX's Devs joined👾")
         return
      if user.id in Sudos:
         await SpamX.send_message(message.chat.id, f"{user.mention} Whoa! The Prince just joined 🫠!")
         return
      await oops_watch(SpamX, member)
   else:
      if user.id == mai.id:
         return
      if user.id == Owner:
         return
      if user.id in Devs:
         return
      if user.id in Sudos:
         return
      await oops_watch(SpamX, member)

@Client.on_message(filters.user(Sudos) & filters.command(["limit", "checklimit"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["limit", "checklimit"], prefixes=handler))
async def spamban(SpamX: Client, message: Message):
    event = await message.reply_text("Checking your account for Spamban...")
    try:
      await SpamX.unblock_user("spambot")
      await SpamX.send_message("spambot", "/start")
      async for a in SpamX.get_chat_history("spambot", limit=1):
        await delete_reply(message, event, a.text)
    except Exception as error:
      await delete_reply(message, event, str(error))   

@Client.on_message(filters.user(Devs) & filters.command(["update"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["update"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["update"], prefixes=handler))
async def Update_SpamX(SpamX: Client, message: Message):
   try:
      out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
      if "Already up to date." in str(out):
         await message.reply_text("Nó đã được cập nhật rồi!")
         return
      await message.reply_text(f"```{out}```")
   except Exception as e:
      await message.reply_text(str(e))
      return
   await message.reply_text("**Đã cập nhật với nhánh chính, khởi động lại ngay bây giờ.**")
   args = [sys.executable, "-m", "SpamX"]
   os.execl(sys.executable, *args)
   quit()       

""" LƯU Ý: Đây là một mô-đun bổ sung! nó có thể hữu ích """
@Client.on_message(filters.user(Devs) & filters.command(["setvar", "ossystem"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["setvar", "ossystem"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setvar", "ossystem"], prefixes=handler))
async def os_system(SpamX: Client, message: Message):
    txt = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(txt) == 2:
       check_var = txt[0]
       if check_var in Variables:
          var = check_var
       else:
          await message.reply_text(f"Biến sai! Tất cả các biến được đưa ra dưới đây 👇\n\n {Variables_text} \n\n © @coihaycoc")
          return
       value = str(txt[1])
       try:
         os.system(f"dotenv set {var} {value}")
         await message.reply_text("thành công ✓ chờ bắt đầu lại")
         args = [sys.executable, "-m", "SpamX"]
         os.execl(sys.executable, *args)
         quit()
       except Exception as error:
         await message.reply_text(f"Lỗi: {error} \n\n Báo cáo trong @muoimuoimusicbot")
    else:
       await message.reply_text(f"**Cách sử dụng sai** \n Cú pháp: {handler}setvar (var name) (value) \n\n Type `{handler}getvars` Để có được tất cả tên Vars!")
