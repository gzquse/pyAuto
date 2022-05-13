from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# 建立一个浏览器对象
driver = webdriver.Firefox()
# 启动页面
driver.get('https://www.baidu.com')
# driver.set_window_size(800,600)
# driver.find_element_by_id('kw').send_keys('万门大学')
# driver.find_element_by_id('su').click()
# driver.implicitly_wait(10)
#
setup = driver.find_element_by_id('s-usersetting-top')
#
ActionChains(driver).move_to_element(setup).perform()
print(driver.current_window_handle)  # 当前页面的id
# driver.find_element_by_link_text('高级搜索').click()
#
# sleep(2)
# driver.find_element_by_id('adv_keyword').send_keys('132131')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/a[5]').click()
allwindows = driver.window_handles
driver.switch_to.window(allwindows[-1])
print(driver.current_window_handle)

# /html/body/div[1]/div[6]/div/div/div/div[2]/div/form/ul/li[1]/div[3]/span
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/a[5]').click()
#
# allwindows = driver.window_handles
# driver.switch_to.window(allwindows[-1])
# sleep(2)
# driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[1]/div/div/p[1]/a').click()
driver.find_element_by_link_text('英雄联盟吧').click()

# print(driver.current_window_handle)


# driver.find_element_by_id('kw').send_keys('abcd')
# driver.implicitly_wait(10)
# driver.find_element_by_id('su').click()
