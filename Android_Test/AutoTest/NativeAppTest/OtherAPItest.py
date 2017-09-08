# /usr/bin/python
# -*- coding:utf8 -*-

from appium import webdriver
import unittest
import time

class MyTestCase(unittest.TestCase):

	# 脚本初始化，获取操作实例
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = '192.168.135.101:5555'

		# Appium框架API讲解与实践(一)(二)
		#desired_caps['appPackage'] = 'com.android.calculator2'
		#desired_caps['appActivity'] = '.Calculator'

		# Appium框架API讲解与实践(三)(四)
		#desired_caps['appPackage'] = 'com.android.customlocale2'
		#desired_caps['appActivity'] = '.CustomLocaleActivity'

		# Appium框架API讲解与实践(五)
		desired_caps['appPackage'] = 'com.xio.cardnews'
		desired_caps['appActivity'] = 'com.xio.cardnews.activity.MainActivity'

		desired_caps['unicodeKeyboard'] = 'True'
		desired_caps['resetKeyboard'] = 'True'

		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


	# 释放实例，释放资源
	def tearDown(self):
		self.driver.quit()

	# 测试的脚本

	def testOtherAPI(self):
		
		# find_elements_by_id
		elements = self.driver.find_elements_by_id('digit_8')
		elements[0].click()
		time.sleep(5)
		print(len(elements))

		# find_element_by_accessibility_id
		self.driver.find_element_by_id('digit_1').click()
		self.driver.find_element_by_id('digit_0').click()
		element = self.driver.find_element_by_accessibility_id(u'除').click()
		self.driver.find_element_by_id('digit_5').click()
		self.driver.find_element_by_id('eq').click()
		time.sleep(5)

		#self.driver.press_keycode(8)
		#self.driver.press_keycode(7)

		# send_keys
		# press_keycode
		self.driver.find_element_by_id('formula').send_keys('10')
		# 通过content_desc查找
		element = self.driver.find_element_by_accessibility_id(u'除').click()
		self.driver.press_keycode(12)
		self.driver.find_element_by_id('eq').click()
		time.sleep(5)

	def testMoreAPI(self):
		# 获取元素列表
		#els = self.driver.find_elements_by_class_name('android.widget.CheckedTextView')

		# 滚动scroll的用法
		#self.driver.scroll(els[7],els[3])

		# 拖动drag_and_drop的用法
		#self.driver.drag_and_drop(els[7],els[3])

		# 滑动swipe的用法
		#self.driver.swipe(100,750,100,100)

		# 点击tap的用法
		#self.driver.tap([(100,750)])

		# 快速滑动flick的用法
		#self.driver.flick(100,750,100,100)

		# 查看当前activity的用法
		#print(self.driver.current_activity)

		# 等待指定activity显示
		# 3为等待时间，1为检测间隔
		#print(self.driver.wait_activity('.CustomLocaleActivity',3,1))

		# 将某一个App置于后台
		#self.driver.background_app(3)

		# 判断app是否安装了
		#print(self.driver.is_app_installed('com.xio.cardnews'))

		# 卸载app
		#self.driver.remove_app('com.xio.cardnews')

		# 安装app
		#self.driver.install_app('C:/Users/ThinkPad/Desktop/cardnews.apk')

		# 启动app
		self.driver.close_app()
		self.driver.launch_app()

		# 启动activity
		self.driver.start_activity('com.xio.cardnews','com.xio.cardnews.activity.MainActivity')

		# 截屏
		time.sleep(3)
		self.driver.get_screenshot_as_file('test.png')
		time.sleep(5)



if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(MyTestCase('testMoreAPI'))
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
