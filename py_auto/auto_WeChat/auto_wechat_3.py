# 开启微信控制 -  自动回复
from WechatPCAPI import WechatPCAPI
import time
import os


def on_messages(message):
    global wx_inst
    print(message)
    try:
        # 做一个非个人用户的判断
        if message['data']['from_wxid'] not in ['floatbottle','medianote']:
            # 做一个简单的关键词 + 接收信息的判断（0接收 1发出）
            if message['data']['msg'] in ['你好','在吗?','?','在不在'] and message['data']['send_or_recv'][0] == '0':
                wx_inst.send_text(to_user=message['data']['from_wxid'],msg='你好， 我在！ 有什么可以帮您的？')
    except:
        print('数据条件不满足')
        print(message)


wx_inst = WechatPCAPI(on_message=on_messages)

# 启动微信
wx_inst.start_wechat(block=True)
# 等待登陆成功，此时需要人为扫码登录微信
while not wx_inst.get_myself():
    time.sleep(5)
print('登陆成功')
