# /usr/bin/python
# -*- coding:utf-8 -*-

import os
import time
import csv


# 控制类
class Controller(object):
	# 初始化
	def __init__(self, count):
		self.count = count
		self.allData = [('currenttime','batterylevel')]

	# 单次测试过程
	def testprocess(self):
		result = os.popen('adb shell dumpsys battery')
		for line in result.readlines():
			if 'level' in line:
				batterylevel = int(line.split(':')[1])

		currenttime = self.getCurrentTime()
		self.allData.append((currenttime,batterylevel))

	def run(self):
		# 设置手机进入非充电状态
		# os.popen('adb shell dumpsys battery set status 1')
		while self.count > 0:
			self.testprocess()
			self.count = self.count - 1
			time.sleep(10)

	def getCurrentTime(self):
		CurrentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		return CurrentTime

	def SaveDataToCSV(self):
		csvfile = open('batteryinfo.csv','w')
		writer = csv.writer(csvfile)
		writer.writerows(self.allData)
		csvfile.close()

if __name__ == '__main__':
	controller = Controller(12)
	controller.run()
	controller.SaveDataToCSV()
