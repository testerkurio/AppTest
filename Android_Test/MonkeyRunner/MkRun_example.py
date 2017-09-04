#!/usr/bin/python
# -*- coding:utf8 -*-

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

# 连接设备
device = MonkeyRunner.waitForConnection(3,'1849cdbf')

# 启动App
device.startActivity('com.android.browser/com.android.browser.BrowserActivity')
MonkeyRunner.sleep(2)

# 点击搜索框
device.touch(409,351,'DOWN_AND_UP')
MonkeyRunner.sleep(1)

#输入查询词
device.type('test')
MonkeyRunner.sleep(1)

#点击回车键
#device.press('KEYCODE_ENTER','DOWN_AND_UP')
#MonkeyRunner.sleep(1)

#点击搜索按钮
device.touch(982,143,'DOWN_AND_UP')
MonkeyRunner.sleep(6)

#截图
image = device.takeSnapshot()
image.writeToFile('./test.png','png')

