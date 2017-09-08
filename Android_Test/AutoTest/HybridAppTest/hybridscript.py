# /usr/bin/python
# -*- coding:utf8 -*-

import unittest
import time
from appium import webdriver

class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.desired_caps = {}
		self.desired_caps['platformName'] = 'Android'
		self.desired_caps['platformVersion'] = '6.0'
		self.desired_caps['deviceName'] = '192.168.135.101:5555'
		self.desired_caps['appPackage'] = 'mark.via'
		self.desired_caps['appActivity'] = 'mark.via.ui.activity.BrowserActivity'
		self.desired_caps['unicodeKeyboard'] = 'True'
		self.desired_caps['resetKeybboard'] = 'True'
		#self.desired_caps['automationName'] = 'Selendroid'
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.desired_caps)

	def testSearch(self):

		# 进入baidu.com主页
		self.driver.find_element_by_id('b0').click()
		self.driver.find_element_by_class_name('android.widget.EditText').send_keys('baidu.com')
		self.driver.find_element_by_id('b3').click()

		time.sleep(5)

		# switch 切换当前的上下文
		print(self.driver.contexts) # contexts包含了native和webview两部分
		# 切换到webview部分
		self.driver.switch_to.context('WEBVIEW_mark.via') # 为contexts值的后部分
		print(self.driver.current_context)

		time.sleep(3)

		# 测试其他API
		# 定位元素组
		elements = self.driver.find_elements_by_xpath('//*[@id="ns-swipe"]/div/div[1]')
		# 输出所有元素的名称
		for el in elements:
			print(el.text)
		
		time.sleep(5)

		# 在百度页面搜索内容
		# 定位web输入框
		webinput = self.driver.find_element_by_xpath('//*[@id="index-kw"]')
		webinput.click()
		webinput.send_keys('mook')
		self.driver.find_element_by_xpath('//*[@id="index-bn"]').click()
		time.sleep(5)

		# 检验查询结果
		firstresult = self.driver.find_element_by_xpath('//*[@id="results"]/div[1]/div[1]/a[1]/h3')
		self.assertTrue(u'百度百科' in firstresult.text)
		

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()