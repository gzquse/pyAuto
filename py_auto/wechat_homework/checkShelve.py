#查看保存的好友

import shelve,os


print('我的朋友数据')
my_friends = shelve.open('friends.db',writeback=True)
for x,y in my_friends.items():
    print(x,y)
    print('wxid',y['wx_id'])
    print('昵称',y['remark_name'])
