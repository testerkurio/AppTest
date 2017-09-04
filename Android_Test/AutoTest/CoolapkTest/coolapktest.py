# /usr/bin/python
# -*- coding:utf-8 -*-

import time
from appium import webdriver

# 脚本初始化
# 定义设备属性
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '192.168.135.101:5555'

# 定义被测程序属性
desired_caps['appPackage'] = 'com.coolapk.market'
desired_caps['appActivity'] = 'com.coolapk.market.view.main.MainActivity'

# 定义中文环境编码
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'

# 将属性传给appium的API接口，以实现脚本-appium-App的交互
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# 控制操作手机
driver.find_element_by_id('toolbar_search_text').click()
driver.find_element_by_id('search_text').send_keys('美丽修行')
driver.find_element_by_id('search_button').click()

# 验证结果
try:
	if driver.find_element_by_id('toolbar_search_text').is_displayed():
		print('fail')
except Exception as e:
	print(e)
	print('pass')

# 将资源释放
driver.quit()

# 为每一步的间隔
time.sleep(3)

