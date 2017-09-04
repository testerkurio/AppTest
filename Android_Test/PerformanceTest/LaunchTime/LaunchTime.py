#/usr/bin/python
# -*- coding:utf-8 -*-

import os
import csv
import time

# app类
class App(object):
	# 初始化
	def __init__(self):
		self.content = ''
		self.startTime = 0

	# 启动App
	def LaunchApp(self):
		cmd = 'adb shell am start -W -n com.coolapk.market/.view.main.MainActivity'
		# os.popen(cmd)会把执行的cmd的输出作为值返回
		self.content = os.popen(cmd) 

	# 停止App
	def StopApp(self):
		#cmd = 'adb shell am force-stop com.coolapk.market'
		cmd = 'adb shell input keyevent 3'
		os.popen(cmd)

	# 获取启动时间
	def GetLaunchedTime(self):
		# 使用关键字获取启动时间
		for line in self.content.readlines():
			if 'ThisTime' in line:
				self.startTime = line.split(':')[1]
				break
		return self.startTime

# 控制类
class Controller(object):
	# 初始化
	def __init__(self,count):
		#  获取App类的实例
		self.app = App()
		self.counter = count
		self.alldata = [('timestamp','elpasedtime')]

	# 单次测试过程
	def testprocess(self):
		# 启动App
		self.app.LaunchApp()
		# 获取启动时间
		time.sleep(5)
		elpasedtime = self.app.GetLaunchedTime()
		# 停止App
		self.app.StopApp()
		# 获取当前时间戳
		time.sleep(3)
		currenttime = self.getCurrentTime()
		# 记录当前时间和启动时间
		self.alldata.append((currenttime,elpasedtime))

	# 多次执行测试过程
	def run(self):
		while self.counter > 0:
			self.testprocess()
			self.counter = self.counter - 1

	# 获取当前的时间戳
	def getCurrentTime(self):
		currentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
		return currentTime

	# 数据的存储
	def SaveDataToCSV(self):
		# 打开一个csv文件
		csvfile = open('startTime2.csv','w') # w为写模式，b为二进制模式
		# 写入数据
		writer = csv.writer(csvfile)
		writer.writerows(self.alldata)
		# 关闭csv文件
		csvfile.close()


# 如果是直接调用就执行
if __name__ == '__main__':
	# 创建控制类实例
	controller = Controller(10)
	# 运行多次循环
	controller.run()
	# 保存数据
	controller.SaveDataToCSV()
