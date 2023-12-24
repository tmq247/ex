"""
   © RiZoeLX 
   SpamX - Telegram Bots
"""


import os, sys, asyncio, random
from random import choice
from .. import Owner, handler, Sudos

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired, RightForbidden, RPCError, UserNotParticipant
from pyrogram.enums import ChatType

from RiZoeLX import Devs
from RiZoeLX.functions import user_reason, user_only, get_user

@Client.on_message(filters.group & filters.user(Sudos) & filters.command(["ban"], prefixes=handler))
@Client.on_message(filters.group & filters.me & filters.command(["ban"], prefixes=handler))
async def ban_user(SpamX: Client, message: Message):  
   user, reason = await user_reason(SpamX, message, Owner, Sudos)
   try:
      await SpamX.ban_chat_member(message.chat.id, user.id)
   except ChatAdminRequired:
      await message.reply_text("Tôi không phải là quản trị viên hoặc tôi không có quyền.")
      return
   except RightForbidden:
      await message.reply_text("Tôi không có đủ quyền để cấm người dùng này.")
      return 
   except UserNotParticipant:
      await message.reply_text("Làm cách nào tôi có thể cấm người dùng không tham gia cuộc trò chuyện này?")
      return 
   except RPCError as eror:
      await message.reply_text(str(eror))
      return 

   if reason:
      await message.reply_text(f"Đã cấm {user.mention}! \nLý do: {reason}")
   else:
      await message.reply_text(f"Đã cấm {user.mention}!")


@Client.on_message(filters.group & filters.user(Sudos) & filters.command(["unban"], prefixes=handler))
@Client.on_message(filters.group & filters.me & filters.command(["unban"], prefixes=handler))
async def unban_user(SpamX: Client, message: Message):  
   user = await get_user(SpamX, message)
   try:
      await SpamX.unban_chat_member(message.chat.id, user.id)
   except ChatAdminRequired:
      await message.reply_text("Tôi không phải là quản trị viên hoặc tôi không có quyền.")
      return
   except RightForbidden:
      await message.reply_text("Tôi không có đủ quyền để cấm người dùng này.")
      return  
   except RPCError as eror:
      await message.reply_text(str(eror))
      return 
   await message.reply_text(f"Bỏ cấm {user.mention}! \nLý do: {reason}")

@Client.on_message(filters.group & filters.user(Sudos) & filters.command(["promote"], prefixes=handler))
@Client.on_message(filters.group & filters.me & filters.command(["promote"], prefixes=handler))
async def promote_user(SpamX: Client, message: Message):
   chat = message.chat
   user = await get_user(SpamX, message)
   try:
     await SpamX.promote_chat_member(chat.id, user.id,
          can_change_info=False,
          can_post_messages=True,
          can_edit_messages=True,
          can_delete_messages=True,
          can_restrict_members=False,
          can_invite_users=True,
          can_pin_messages=True,
          can_promote_members=False,
          )
     await message.reply_text(f"Promoted {user.mention}!")
   except ChatAdminRequired:
     await message.reply_text("Tôi không phải là quản trị viên hoặc tôi không có quyền.")
   except RightForbidden:
     await message.reply_text("Tôi không có đủ quyền để cấm người dùng này.")
   except UserNotParticipant:
     await message.reply_text("Làm cách nào tôi có thể thăng chức cho người dùng không tham gia cuộc trò chuyện này?")
   except RPCError as eror:
     await message.reply_text(str(eror))


@Client.on_message(filters.group & filters.user(Sudos) & filters.command(["fullpromote", "fpromote"], prefixes=handler))
@Client.on_message(filters.group & filters.me & filters.command(["fullpromote", "fpromote"], prefixes=handler))
async def fullpromote(SpamX: Client, message: Message):
   chat = message.chat
   user = await get_user(SpamX, message)
   try:
     await SpamX.promote_chat_member(chat.id, user.id,
            #is_anonymous=False,
            can_change_info=True,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=True,
            )
     await message.reply_text(f"Thăng chức full {user.mention}!")
   except ChatAdminRequired:
     await message.reply_text("Tôi không phải là quản trị viên hoặc tôi không có quyền.")
   except RightForbidden:
     await message.reply_text("Tôi không có đủ quyền để cấm người dùng này.")
   except UserNotParticipant:
     await message.reply_text("Làm cách nào tôi có thể thăng chức người dùng không tham gia cuộc trò chuyện này?")
   except RPCError as eror:
     await message.reply_text(str(eror))

@Client.on_message(filters.group & filters.user(Sudos) & filters.command(["demote"], prefixes=handler))
@Client.on_message(filters.group & filters.me & filters.command(["demote"], prefixes=handler))
async def demote_user(SpamX: Client, message: Message):
   chat = message.chat
   user = await get_user(SpamX, message)
   try:
     await SpamX.promote_chat_member(chat.id, user.id,
            is_anonymous=False,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            )
     await message.reply_text(f"Demote {user.mention}!")
   except ChatAdminRequired:
     await message.reply_text("Tôi không phải là quản trị viên hoặc tôi không có quyền.")
   except RightForbidden:
     await message.reply_text("Tôi không có đủ quyền để cấm người dùng này.")
   except UserNotParticipant:
     await message.reply_text("Làm cách nào tôi có thể hạ chức cho người dùng không tham gia cuộc trò chuyện này?")
   except RPCError as eror:
     await message.reply_text(str(eror))

@Client.on_message(filters.group & filters.user(Sudos) & filters.command(["pin"], prefixes=handler))
@Client.on_message(filters.group & filters.me & filters.command(["pin"], prefixes=handler))
async def pin_message(SpamX: Client, message: Message): 
   reply = message.reply_to_message
   if not reply:
     await message.reply_text("Trả lời tin nhắn!")
     return
   try:
     await SpamX.pin_chat_message(message.chat.id, reply.id)
     await message.reply_text("Pinned 📌")
   except ChatAdminRequired:
     await message.reply_text("Tôi không phải là quản trị viên hoặc tôi không có quyền.")
   except RightForbidden:
     await message.reply_text("Tôi không có đủ quyền để cấm người dùng này.")
   except UserNotParticipant:
     await message.reply_text("Làm cách nào tôi có thể thăng chức người dùng không tham gia cuộc trò chuyện này?")
   except RPCError as eror:
     await message.reply_text(str(eror))

@Client.on_message(filters.group & filters.user(Sudos) & filters.command(["unpin"], prefixes=handler))
@Client.on_message(filters.group & filters.me & filters.command(["unpin"], prefixes=handler))
async def unpin_message(SpamX: Client, message: Message):
   reply = message.reply_to_message
   if not reply:
     await message.reply_text("Trả lời tin nhắn!")
     return
   try:
     await SpamX.unpin_chat_message(message.chat.id, reply.id)
     await message.reply_text("Unpinned!")
   except ChatAdminRequired:
     await message.reply_text("Tôi không phải là quản trị viên hoặc tôi không có quyền.")
   except RightForbidden:
     await message.reply_text("Tôi không có đủ quyền để cấm người dùng này.")
   except UserNotParticipant:
     await message.reply_text("Làm cách nào tôi có thể quảng bá cho người dùng không tham gia cuộc trò chuyện này?")
   except RPCError as eror:
     await message.reply_text(str(eror))


@Client.on_message(filters.group & filters.user(Sudos) & filters.command(["purge", "purges", "p"], prefixes=handler))
@Client.on_message(filters.group & filters.me & filters.command(["purge", "purges", "p"], prefixes=handler))
async def _purges(SpamX: Client, message: Message):
    if message.chat.type not in [ChatType.SUPERGROUP, ChatType.CHANNEL]:
        return

    status_message = await message.reply_text("...", quote=True)
    message_ids = []
    count_del_etion_s = 0

    if message.reply_to_message:
        for a_s_message_id in range(
            message.reply_to_message.id, message.id
        ):
            message_ids.append(a_s_message_id)
            if len(message_ids) == 100:
                count_del_etion_s += await SpamX.delete_messages(
                    chat_id=message.chat.id, message_ids=message_ids, revoke=True
                )
                message_ids = []
        if len(message_ids) > 0:
            count_del_etion_s += await SpamX.delete_messages(
                chat_id=message.chat.id, message_ids=message_ids, revoke=True
            )

    await status_message.edit_text(f"deleted {count_del_etion_s} messages")
    await asyncio.sleep(5)
    await status_message.delete()
