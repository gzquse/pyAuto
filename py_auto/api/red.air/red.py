# -*- encoding=utf8 -*-
__author__ = "GAO"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# poco(text='微信').click()

Chat_msg=poco("com.tencent.mm:id/dg2").offspring("com.tencent.mm:id/e3x") 
 
for x in Chat_msg:
    print(x.get_text())
    if 'the test chatroom' in x.get_text():
        print('the test chatroom')
        x.click()
             #   寻找红包 所有的
        while True:
            from time import sleep
            sleep(0.1)
            
            red_candidate = poco("com.tencent.mm:id/an3").children()
            for red in red_candidate:
                #h获取 不能零的红包条件
                invalid= red.offspring('com.tencent.mm:id/r0')
                #获取可以领的条件
                get_money = red.offspring('com.tencent.mm:id/r8')
                print(get_money)
                #如果 可以领
                if get_money:
                    #判断不能领是否存在
                    if invalid.exists():
                        print('红包不能领取，已经领过了')
                        print(invalid)
                      #否则就是可以继续
                    else:
                        print('可以领取冲冲冲')
                        print(get_money)
                        get_money.click()
                        sleep(0.4)
                        poco("android.widget.LinearLayout").offspring("com.tencent.mm:id/den").click()
                        keyevent('BACK')        
        



 
# #开 点击领取

# poco("android.widget.LinearLayout").offspring("com.tencent.mm:id/den")

#退出
# poco("android.widget.LinearLayout").offspring("com.tencent.mm:id/dim")

