#/usr/bin/python
# -*- coding:utf-8 -*-

import os
import csv
import time

# App类
class App(object):
	# 初始化
	def __init__(self):
		self.content = ''

	# 启动App
	def LaunchApp(self):
		cmd = 'adb shell am start -W -n com.coolapk.market/.view.main.MainActivity'
		self.content = os.popen(cmd)

	# 停止App/返回HOME界面
	def StopApp(self):
		# cmd = 'adb shell input keyevent 3'
		cmd = 'adb shell am force-stop com.coolapk.market'
		os.popen(cmd)

	# 获取当前事件
	def CalculateTime(self):
		currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		return currentTime

# 控制类
class Controller(object):
	# 初始化
	def __init__(self,count):
		self.count = count
		self.app = App()
		self.allData = [('TimeBeforeLaunch','TimeAfterLaunch')]

	# 单次测试过程
	def testprocess(self):
		TimeBeforeLaunch = self.app.CalculateTime()
		self.app.LaunchApp()
		self.app.StopApp()
		TimeAfterLaunch = self.app.CalculateTime()
		self.allData.append((TimeBeforeLaunch,TimeAfterLaunch))
		time.sleep(5)

	# 多次循环
	def run(self):
		while self.count > 0:
			self.testprocess()
			self.count = self.count - 1

	# 存储数据
	def SaveDataToSave(self):
		csvfile = open('StampTime.csv','w')
		writer = csv.writer(csvfile)
		writer.writerows(self.allData)
		csvfile.close()


if __name__ == '__main__':
	controller = Controller(4)
	controller.run()
	controller.SaveDataToSave()

