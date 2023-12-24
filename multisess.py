# SpamX Multiple String Generator 

from pyrogram import Client
#import tgcrypto

ID = int(input(" \n Gửi Api Id để tạo phiên chuỗi: "))
HASH = str(input(" \n Gửi Api Hash để tạo phiên chuỗi: "))

try:
     number_to_add = int(input(" \n Nhập số lượng tài khoản bạn muốn tạo chuỗi:"))
     whom = input(" \n Nhập Tên người dùng hoặc Id người dùng của bạn để Khách hàng có thể chuyển tiếp tất cả các phiên cho bạn nếu không nhấn enter: ")
     for i in range(number_to_add):
            RiZoeL = Client(name="Còi", api_id=ID, api_hash=HASH, in_memory=True)
            RiZoeL.start()
            s = RiZoeL.export_session_string()
            sess = str(s)
            if whom:
                id = RiZoeL.get_users(whom).id
                RiZoeL.send_message(id, f"**Pyrogram String Session** \n\n `{sess}` \n\n © @coihaycoc")
            else:
                RiZoeL.send_message("me", f"**Pyrogram String Session** \n\n `{sess}` \n\n © @coihaycoc")
       
     if whom:
           print(f"Tất cả phiên đã được gửi đến {whom}")
     else:
         print("Tất cả các phiên đã được gửi đến tin nhắn đã lưu")
         
except Exception as a:
   print(a)    
