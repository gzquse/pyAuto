# 开启微信控制 -  自动回复
from WechatPCAPI import WechatPCAPI
import time
import os

# 做两个问答表
key_word = [['你好','在吗?','?','在不在'],['有好课吗','有新课吗','课程'],['有没有小万君','小万君在不在','小万君']]
key_answer = [['您好，您请讲'],['您好，最近万门推出Python基础趣讲精练和Python办公自动化，打折中哦！'],['小万君来啦！，您请说']]


def on_messages(message):
    global wx_inst
    try:
        # 做一个非个人用户的判断
        if message['data']['from_wxid'] not in ['fmessage','filehelper','floatbottle','medianote','newsapp']:
            for word,answer in zip(key_word,key_answer):  # #组合问答表
                # 做一个简单的关键词 + 接收信息的判断（0接收 1发出）
                if message['data']['msg'] in word and message['data']['send_or_recv'][0] == '0':
                    wx_inst.send_text(to_user=message['data']['from_wxid'],msg=answer[0])
                    break
            # 特别注意这里的逻辑 如果for循环正常执行完成， else才会执行，如果中断，else不会执行
            else:
                if message['data']['send_or_recv'][0] == '0':
                    wx_inst.send_text(to_user=message['data']['from_wxid'],msg='额滴个神你在说什么火星语！')
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
