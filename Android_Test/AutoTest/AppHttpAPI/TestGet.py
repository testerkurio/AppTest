# /usr/bin/python
# -*- coding:utf8 -*-

import requests
import unittest

class testClass(unittest.TestCase):
	def testGet(self):
		# headers的部分配置
		headers = {
		'User-Agent':'hlj-android/3.3.1',
		'Host':'customers-api.helijia.com',
		'Connection':'Keep-Alive',
		'Accept-Encoding':'gzip'
		}

		# cookies的部分配置
		cookies = dict(
			beacon_id = 'MTAxLjI1MS4xQTUuMTE5LTE0QzZELTUzQkE4OTQ5QjUyMzctNjE',
			search_test = '1',
			search_r = '32'
			)


		# get请求的构造
		res = requests.get('http://coding.imooc.com/lesson/ajaxmediauser/',headers = headers,cookies = cookies)

		print(res.text)
		print(res.status_code)

		self.assertTrue(u'http://img.ucdn.static.helijia.com' in res.text)

if __name__ == '__main__':
	unittest.main()

