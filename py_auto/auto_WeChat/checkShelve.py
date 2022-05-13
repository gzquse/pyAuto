import shelve,os

print('我的朋友数据')
my_friends = shelve.open('friends.db',writeback=True)
for x,y in my_friends.items():
    print(x,y)

print('我的群聊数据')
my_chatroom = shelve.open('chatroom.db',writeback=True)
for x,y in my_chatroom.items():
    print(x,y)
