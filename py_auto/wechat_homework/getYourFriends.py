#todo 先获取你的用户

from WechatPCAPI import WechatPCAPI
import time
import shelve

#做一个持久化对象 shelve保存用户数据
def on_message(message):
    print(message)
    #获取个人 并存入 持久化对象
    my_targeted_friends = shelve.open('friends.db', writeback=True)
    if message['type'] == 'friend::person':
        if message['data']['wx_id'] not in ['fmessage','filehelper','floatbottle','medianote','newsapp']:
            my_targeted_friends[message['data']['wx_id']] =  message['data']
    my_targeted_friends.close()

#启动主微信控制
def main_wechat_control():
    # 初始化微信实例    #注意这个是一个回调函数，即如果wx inst完成了任务，会执行on_message函数，并带入参数
    wx_inst = WechatPCAPI(on_message=on_message)
     # 启动微信
    wx_inst.start_wechat(block=True)
    # 等待登陆成功，此时需要人为扫码登录微信
    while not wx_inst.get_myself():
        time.sleep(5)

    wx_inst.update_frinds() #注意这里 需要使用一下更新好友列表，比如你的备注remark 昵称nickname


if __name__ == '__main__':
    main_wechat_control()