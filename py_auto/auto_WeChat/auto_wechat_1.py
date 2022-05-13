# todo 先获取你的用户

from WechatPCAPI import WechatPCAPI
import time
import shelve


# 做一个持久化对象 shelve保存用户数据
def on_message(message):
    print(message)
    # 获取个人
    my_targeted_friends = shelve.open('friends1.db',writeback=True)
    if message['type'] == 'friend::person':
        my_targeted_friends[message['data']['wx_id']] = message['data']['wx_nickname']
    my_targeted_friends.close()

    # 获取群聊
    my_targeted_chatroom = shelve.open('chatroom1.db',writeback=True)
    if message['type'] == 'friend::chatroom':
        my_targeted_chatroom[message['data']['chatroom_id']] = message['data']['chatroom_name']
    my_targeted_chatroom.close()


# 启动主微信控制
def main_wechat_control():
    # 初始化微信实例    #注意这个是一个回调函数，即如果wx inst完成了任务，会执行on_message函数，并带入参数
    wx_inst = WechatPCAPI(on_message=on_message)
    # 启动微信
    wx_inst.start_wechat(block=True)
    # 等待登陆成功，此时需要人为扫码登录微信
    while not wx_inst.get_myself():
        time.sleep(5)


if __name__ == '__main__':
    main_wechat_control()
