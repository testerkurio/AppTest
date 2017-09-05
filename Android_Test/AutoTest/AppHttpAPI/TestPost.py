# /usr/bin/python
# -*- coding:utf8 -*-

import requests
import unittest

class testClass(unittest.TestCase):
	def testPost(self):
		# requests body数据
		keyword = {
		'version':'3.3.1',
		'city':'110100',
		'requestTime':'1472980321726',
		'deviceType':'android',
		'device_id':'d3c1d53d0a8a378f',
		'w':'{"widgets":[{"defaultParams":}]}'
		}

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
		res = requests.post('http://coding.imooc.com/lesson/ajaxmediauser/',
		data = keyword, headers = headers, cookies = cookies)

		print(res.text)
		print(res.status_code)

		self.assertTrue(u'成功' in res.text)

if __name__ == '__main__':
	unittest.main()

