# 开启微信控制 -  群发消息对个人
from WechatPCAPI import WechatPCAPI
import time
import shelve
import os

my_friends = shelve.open('friends.db')


def on_messages(messsage):
    print(messsage)


wx_inst = WechatPCAPI(on_message=on_messages)
# 启动微信
wx_inst.start_wechat(block=True)
# 等待登陆成功，此时需要人为扫码登录微信
while not wx_inst.get_myself():
    time.sleep(5)
print('登陆成功')

while True:
    msg = input('想给你的朋友们说点儿啥？')
    if msg == 'q':
        exit()
    for wxid,nickname in my_friends.items():
        wx_inst.send_text(to_user=wxid,msg=msg)
        wx_inst.send_file(to_user=wxid,file_abspath=os.path.abspath('myfile.txt'))
        time.sleep(1)
        wx_inst.send_img(to_user=wxid,img_abspath='C:/Users/MartinLovesFey/python/py_auto/auto_WeChat/logo.jpg')
        time.sleep(1)
    # 微信群信息发送
    wx_inst.send_text(to_user='23175794361@chatroom',msg='group test run',at_someone='MasterVader')
