""" RiZoeLX 2022-2023 © SpamX """

import re


def user_errors(error):
    if '[400 USERNAME_NOT_OCCUPIED]' in str(error):
       return "Bạn chưa cung cấp tên người dùng"
    elif '[400 USERNAME_INVALID]' in str(error):
       return "Tên người dùng không hợp lệ"
    elif '[400 PEER_ID_INVALID]' in str(error):
       return "ID người dùng không hợp lệ!"
    else:
       return f"**Lỗi không rõ:** \n\n {error}"

def join_errors(error):
    if '[400 USERNAME_NOT_OCCUPIED]' in str(error):
       return "Bạn chưa cung cấp tên người dùng để tham gia!"
    elif '[400 USERNAME_INVALID]' in str(error):
       return "Ahh.. Tên người dùng không hợp lệ"
    elif '[400 INVITE_REQUEST_SENT]' in str(error):
       return "Đã gửi yêu cầu tham gia!"
    elif 'Username not found' in str(error):
       return "Tôi bị cấm vào nhóm đó 🫠"
    else:
       return f"**Lỗi không rõ:** \n\n {error}" 

def leave_errors(error):
    if '[400 PEER_ID_INVALID]' in str(error):
       return "ID trò chuyện sai!"
    elif '[400 USER_NOT_PARTICIPANT]' in str(error):
       return "Tôi không ở trong nhóm đó 🫠"
    elif '[400 USERNAME_INVALID]' in str(error):
       return "Ahh.. Tên người dùng không hợp lệ"
    else:
       return f"**Lỗi không rõ:** \n\n {error}" 
