""" © RiZoeLX """

from .config import *
from .database import *
from .core import *
from pyrogram import Client 
from RiZoeLX.functions import * # make_list
import time, os, sys


print("""
     ╒══════════════════════╕
        Starting Your SpamX 
     ╘══════════════════════╛
""")

#__version__ = "v0.5"
"""start time"""
start_time  = time.time()

try:
   OWNER_ID = int(OWNER_ID)
except ValueError:
   raise Exception("Biến OWNER_ID của bạn không phải là số nguyên hợp lệ.")

"""Sudo Users"""
sudoser = []
if SUDO_USERS:
  sudoser = make_list(OWNER_ID, SUDO_USERS)
else:
  sudoser.append(OWNER_ID)

AUTO_REACT = []
if auto_re:
   AUTO_REACT = make_list(-1002111116005, auto_re)
else:
   AUTO_REACT.append(-1002111116005)

EMOJI_LIST = ['❤️', '✨', '🔥', '🥰', '💫', '💯', '🌟', '😁', '💥']
