# /usr/bin/python
# -*- coding:utf-8 -*-

import unittest

class MyTtestCase(unittest.TestCase):
	
	def setUp(self):
		print('setup')

	def test_something(self):
		print('test_something')
		#断言，判断结果的pass还是fail
		self.assertEqual(True,False)

	def test_anything(self):
		print('test_anything')
		self.assertEqual(True,True)

	def tearDown(self):
		print('teardown')


if __name__ == '__main__':
	unittest.main()