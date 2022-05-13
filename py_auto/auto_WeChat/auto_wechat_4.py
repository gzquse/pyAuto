#开启微信控制 -  控制电脑
from WechatPCAPI import WechatPCAPI
import time
import os


def on_messages(message):
    global wx_inst
    print(message)
    try:
        # 锁定 文件助手 作为与电脑控制的通道
        if message['data']['from_wxid'] == 'filehelper' and 'Phone' in message['data']['send_or_recv']:
            #判断从手机发出的指令才会执行
            print(message)
            print('执行任务')
            wx_inst.send_text(to_user='filehelper', msg='任务执行中')
            # os.system('shutdown /s')
            print('shutdown')
            time.sleep(2) #具体的任务代码
            wx_inst.send_text(to_user='filehelper', msg='任务执行完成')
    except:
        print('数据条件不满足')


wx_inst = WechatPCAPI(on_message=on_messages)

 # 启动微信
wx_inst.start_wechat(block=True)
# 等待登陆成功，此时需要人为扫码登录微信
while not wx_inst.get_myself():
    time.sleep(5)
print('登陆成功')

