#/usr/bin/python
# -*- coding:utf8 -*-

import os
import csv
import time

# 控制类
class Controller(object):
	def __init__(self,count):
		self.counter = count
		self.alldata = [('timestamp','traffic')]

	# 单次测试过程
	def  testprocess(self):
		# 获取查询pid的结果
		result = os.popen('adb shell ps | findstr com.open.mooc')
		# 获取pid
		pid = result.readlines()[0].split(' ')[3]

		# 获取流量
		traffic = os.popen('adb shell cat /proc/' + pid + '/net/dev')
		for line in traffic:
			if 'wlan0' in line:
				# 将所有空格替换成#
				line = '#'.join(line.split())
				# 按#号拆分，获取收到和发出的流量
				receive = line.split('#')[1]
				transmit = line.split('#')[9]
				break
		alltraffic = int(receive) + int(transmit)
		alltraffic = int(alltraffic/1024)
		currenttime = self.getCurrentTime()
		self.alldata.append((currenttime,alltraffic))

	# 多次循环
	def run(self):
		while self.counter > 0:
			self.testprocess()
			self.counter = self.counter - 1
			time.sleep(5)

	# 获取当前时间戳
	def getCurrentTime(self):
		currenttime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		return currenttime

	# 数据的存储
	def SaveDataToCSV(self):
		csvfile = open('traffic.csv','w')
		writer = csv.writer(csvfile)
		writer.writerows(self.alldata)
		csvfile.close()

if __name__ == '__main__':
	controller = Controller(5)
	controller.run()
	controller.SaveDataToCSV()

