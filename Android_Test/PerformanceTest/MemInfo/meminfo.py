# /usr/bin/python
# -*- coding:utf-8 -*-

import os
import csv
import time

# 控制类
class Controller(object):
	def __init__(self):
		self.allData = [('ID','VSS','RSS')]

	def analyzedata(self):
		content = self.readfile()
		i = 0
		for line in content:
			if 'com.coolapk.market' and '1744' in line:
				print(line)
				line = '#'.join(line.split())
				VSS = line.split('#')[7].split('K')[0] #将后面的K去除
				RSS = line.split('#')[8].split('K')[0]

				self.allData.append((i,VSS,RSS))
				i = i + 1

	def SaveDataToCSV(self):
		csvfile = open('meminfo.csv','w')
		writer = csv.writer(csvfile)
		writer.writerows(self.allData)
		csvfile.close()

	def readfile(self):
		mfile = open('meminfo','r')
		content = mfile.readlines()
		mfile.close()
		return content

if __name__ == '__main__':
	controller = Controller()
	controller.analyzedata()
	controller.SaveDataToCSV()
