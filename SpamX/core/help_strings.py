import os, re


hndlr = os.getenv("HNDLR")
if not hndlr:
  hndlr = "."

help_text = f"""
**Menu trợ giúp của SpamX!**

Chức năng/Mô-đun có sẵn ⬇️

=> `spam` , `raid` , `owner` , `directmessage` , `admin` , `core` , `sudos` , `global` , `profile` , `joinleave` , `info`

Kiểu `{hndlr}help` (Tên mô-đun) | Bot sẽ cung cấp thông tin/cách sử dụng
mô-đun đó.

Ví dụ: `{hndlr}help core`
"""

spam_text = f"""
**Tên mô-đun: Spam**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}spam [số lần] [tin nhắn] 
•) {hndlr}delayspam [độ trễ tính bằng giây.] [số lần] [tin nhắn]
•) {hndlr}pornspam [số lần]
•) {hndlr}hange [số lần]
•) {hndlr}uspam [tin nhắn]
•) {hndlr}abuse [số lần hoặc leave]
"""

raid_text = f"""
**Tên mô-đun: Raid**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}raid [số lần] [tên người dùng hoặc trả lời người dùng]
•) {hndlr}uraid [Tên người dùng hoặc trả lời người dùng]
•) {hndlr}replyraid [tên người dùng hoặc trả lời người dùng]
•) {hndlr}dreplyraid [tên người dùng hoặc trả lời người dùng]
"""

dm_text = f"""
**Tên mô-đun: Direct Message**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}dm [tên người dùng hoặc trả lời người dùng] [tin nhắn]
•) {hndlr}dmspam [người dùng] [số lần] [tin nhắn]
•) {hndlr}dmraid [số lần] [tên người dùng hoặc trả lời người dùng]
"""

admin_text = f"""
**Tên mô-đun: Admin**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}ban [người dùng]
•) {hndlr}unban [người dùng]
•) {hndlr}promote [người dùng]
•) {hndlr}demote [người dùng]
•) {hndlr}pin [trả lời tin nhắn]
•) {hndlr}unpin [trả lời tin nhắn]
•) {hndlr}purge [trả lời tin nhắn]
"""

core_text = f"""
**Tên mô-đun: Core**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}report [người dùng] [R7 ban code] [telegraph link as proof]
•) {hndlr}stats
•) {hndlr}setvar [var name] [key value] (Nó có thể hữu ích)
•) {hndlr}getvar (để có được tất cả tên Vars)
•) {hndlr}limit (để kiểm tra giới hạn @Spambot)
•) {hndlr}telegraph [trả lời media]
"""

sudos_text = f"""
**Module name: Sudos**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}addsudo [người dùng] (Điền vào DATABASE_URL để sử dụng suôn sẻ)
•) {hndlr}rmsudo [người dùng] (Điền vào DATABASE_URL để sử dụng suôn sẻ)
•) {hndlr}sudolist
"""

global_text = f"""
**Tên mô-đun: Global**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}gban [user] (Cần có DATABASE_URL trong CMD này)
•) {hndlr}ungban [user] (Cần có DATABASE_URL trong CMD này)
•) {hndlr}gbanlist
•) {hndlr}gpromote [người dùng]
•) {hndlr}gdemote [người dùng]
"""

profile_text = f"""
**Tên mô-đun: Profile**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}setpic [trả lời Media]
•) {hndlr}setname [Tên] [họ (tùy chọn) ]
•) {hndlr}setbio [Bio mới]
•) {hndlr}clone [người dùng] (sao chép hồ sơ của ai đó]
•) {hndlr}revert (Để loại bỏ bản sao)
"""

owner_text = f"""
**Tên mô-đun: Owner stuff**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}eval [code]
•) {hndlr}broadcast [tin nhắn]
•) {hndlr}msgall [tin nhắn] (chỉ trong nhóm)
•) {hndlr}scrape [Từ nhóm] 
•) {hndlr}banall
"""

joinleave_text = f"""
**Tên mô-đun: Join leave**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}join [group username]
•) {hndlr}leave [group username or ID]
"""

info_text = f"""
**Tên mô-đun: Info**

Các lệnh có sẵn và cách dùng ⬇️

•) {hndlr}SpamX
•) {hndlr}info [người dùng]
•) {hndlr}id [người dùng]
"""

def check_string(text):
   if re.search("spam".lower(), text.lower()):
      return "spam"
   if re.search("raid".lower(), text.lower()):
      return "raid"
   if re.search("owner".lower(), text.lower()):
      return "owner"
   if re.search("directmessage|direct_message".lower(), text.lower()):
      return "dm"
   if re.search("admin".lower(), text.lower()):
      return "admin"
   if re.search("core".lower(), text.lower()):
      return "core"
   if re.search("sudos|sudo".lower(), text.lower()):
      return "sudos"
   if re.search("global".lower(), text.lower()):
      return "global"
   if re.search("profile".lower(), text.lower()):
      return "profile"
   if re.search("join|leave|joinleave".lower(), text.lower()):
      return "joinleave"
   if re.search("info".lower(), text.lower()):
      return "info"

async def help_return(text):
   if check_string(text) == "spam":
      return spam_text
   elif check_string(text) == "raid":
      return raid_text
   elif check_string(text) == "dm":
      return dm_text
   elif check_string(text) == "admin":
      return admin_text
   elif check_string(text) == "core":
      return core_text
   elif check_string(text) == "sudos":
      return sudos_text
   elif check_string(text) == "global":
      return global_text
   elif check_string(text) == "profile":
      return profile_text
   elif check_string(text) == "owner":
      return owner_text
   elif check_string(text) == "joinleave":
      return joinleave_text
   elif check_string(text) == "info":
      return info_text
   else:
      return help_text
