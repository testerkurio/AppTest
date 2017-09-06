# /usr/bin/python
# -*- coding:utf8 -*-

from appium import webdriver
import unittest

class MyTestCase(unittest.TestCase):

	# 脚本初始化，获取操作实例
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = '192.168.135.101:5555'
		desired_caps['appPackage'] = 'com.android.calculator2'
		desired_caps['appActivity'] = '.Calculator'
		desired_caps['unicodeKeyboard'] = 'True'
		desired_caps['resetKeyboard'] = 'True'

		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

	# 释放实例，释放资源
	def tearDown(self):
		self.driver.quit()

	# 测试的脚本
	def testAdd(self):

		# locate 定位一个元素
		# operate 操作一个元素
		self.driver.find_element_by_id('digit_8').click()
		self.driver.find_element_by_id('op_add').click()
		self.driver.find_element_by_id('digit_5').click()
		self.driver.find_element_by_id('eq').click()

		# Verify 验证操作的结果
		# Exception 处理异常的情况
		try:
			result = self.driver.find_element_by_id('formula').text
		# self/driver.fin_element_by_class_name('android.widget.EditText')
			self.assertEqual('13',result)
		except Exception:
			print(u'程序出现异常')
			self.fail('程序出现异常')


if __name__ == '__main__':
	unittest.main()
