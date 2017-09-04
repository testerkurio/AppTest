# /usr/bin/python
# -*- coding:utf-8 -*-

import time
from appium import webdriver
import unittest
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
	
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = '192.168.135.101:5555'
		desired_caps['appPackage'] = 'com.coolapk.market'
		desired_caps['appActivity'] = 'com.coolapk.market.view.main.MainActivity'
		desired_caps['unicodeKeyboard'] = 'True'
		desired_caps['resetKeyboard'] = 'True'
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

	@data(('微信',True),('google',True))
	@unpack
	def test_SearchWord(self,searchword,expectedresult):
		self.driver.find_element_by_id('toolbar_search_text').click()
		self.driver.find_element_by_id('search_text').send_keys(searchword)
		self.driver.find_element_by_id('search_button').click()
		time.sleep(5)

		# 验证结果
		try:
			if self.driver.find_element_by_id('item_view').is_displayed():
				exist = True
		except Exception as e:
			exist = False
		#断言，判断结果的pass还是fail
		self.assertEqual(exist,expectedresult)

	def tearDown(self):

		self.driver.quit()


if __name__ == '__main__':
	unittest.main()