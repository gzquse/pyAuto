import os
import win32api
import win32con
from time import sleep

os.popen('dfrgui.exe')
sleep(1)
win32api.keybd_event(9, 0, 0, 0)  # tab
win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键tab

# win32api.keybd_event(9, 0, 0, 0)  # tab
# win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键tab

win32api.keybd_event(13, 0, 0, 0)  # enter
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键enter


