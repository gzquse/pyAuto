# -*- encoding=utf8 -*-
__author__ = "GAO"

from airtest.core.api import *
from time import sleep
auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

 

dev = device()

while True:
    sleep(2)
    try:
        msg=poco('android.widget.LinearLayout').offspring("com.ss.android.ugc.aweme:id/a94")
        print(msg.get_text())
        
    except Exception as e :
        print('****无title***')
        
    finally:
        dev.swipe([305, 1018],[348, 434]) 
