from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import win32api
import win32con

# 实例化一个火狐配置文件
fp = webdriver.FirefoxProfile()
# 设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。

# 设置成0代表下载到浏览器默认下载路径；设置成2则可以保存到指定目录
fp.set_preference("browser.download.folderList",2)

fp.set_preference("browser.download.manager.showWhenStarting",False)
# 下载到指定目录
fp.set_preference("browser.download.dir","C:\\Users\\MartinLovesFey\\python\\py_auto")
fp.set_preference("browser.download.forbid_open_with",True)  # 不打开保存的提示框
fp.set_preference("browser.altClickSave",True)  # 快速保存
# 不询问下载路径；后面的参数为要下载页面的Content-type的值
fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                  "'browser.helperApps.neverAsk.saveToDisk','application/octet-stream ,application/zip,"
                  "application/kswps,application/pdf'")
# 启动一个火狐浏览器进程，以刚才的浏览器参数
driver = webdriver.Firefox(firefox_profile=fp)

# driver = webdriver.Firefox()
sleep(2)
# driver.implicitly_wait(10)
driver.get('https://www.wanmen.org')
# driver.set_window_size(800,600)

user = '18782255301'
pwd = 'gzquse0514'

sleep(3)
# 消除一下 提示框
driver.find_element_by_class_name('containers__btn--Y_DO_').click()
sleep(1)
driver.find_element_by_class_name('components__close-icon--3lRJo').click()

sleep(3)  # 强制sleep
# 点击一下登录按钮
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/div[3]/ul/li[1]/a').click()
sleep(2)

# 选择登录方式
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]').click()

driver.find_element_by_name('account').send_keys(user)

driver.find_element_by_name('password').send_keys(pwd)

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/form/div[4]/button').click()

sleep(3)

search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/input')

search.send_keys('python自动化')

search.send_keys(Keys.ENTER)

print(driver.window_handles)
sleep(2)
driver.find_element_by_class_name('competition__detail-title--2Hl4V').click()

sleep(2)
# 获取所有的window 窗口句柄/就是窗口ID，基于id切换
all_windows = driver.window_handles
print(all_windows)
driver.switch_to.window(all_windows[-1])  # 注意这里需要切换tab/windows
sleep(3)

# 移动窗口 通过js脚本内部执行 完成移动窗口
js_script = 'window.scrollTo(0,500)'  # 左右，上下
driver.execute_script(js_script)

driver.find_element_by_class_name('course__tab-item--13h7q').click()
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div[3]/div').click()

sleep(3)


ds = driver.find_elements_by_class_name('download-button')  # download-button

for x in ds[14:]:
    x.click()
    sleep(3)

    win32api.keybd_event(9,0,0,0)  # tab
    win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)  # 释放按键tab

    win32api.keybd_event(13,0,0,0)  # enter
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)  # 释放按键enter

# 这里特别注意 页面开了新的tab 那么 程序也需要更换
