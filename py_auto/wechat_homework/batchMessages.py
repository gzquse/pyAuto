#开启微信控制 -  群发消息对个人
from WechatPCAPI import WechatPCAPI
import time
import shelve
import os


wx_inst = WechatPCAPI( )
 # 启动微信
wx_inst.start_wechat(block=True)
# 等待登陆成功，此时需要人为扫码登录微信
while not wx_inst.get_myself():
    time.sleep(5)
print('登陆成功')

my_friends = shelve.open('friends.db')
for wxid,y in my_friends.items():
    msg = '来自微信自动化测试(内部)：'+'尊敬的' + y['remark_name'] +'祝您工作顺利！身体健康！'
    wx_inst.send_text(to_user=wxid, msg=msg)

