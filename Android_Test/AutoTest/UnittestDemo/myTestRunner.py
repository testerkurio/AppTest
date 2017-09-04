import unittestrunner
import unittest

'''
# 获取实例
mysuite = unittest.TestSuite()

# 将测试用例加入TestSuite中
mysuite.addTest(unittestrunner.MyTestCase('test_SearchChineseOK'))
mysuite.addTest(unittestrunner.MyTestCase('test_SearchEnglishOK'))

myrunner = unittest.TextTestRunner(verbosity = 2) # 控制log输出级别

# 使用myrunner执行mysuite
myrunner.run(mysuite)
'''



# 以一个类的维度去执行测试用例

cases = unittest.TestLoader().loadTestsFromTestCase(unittestrunner.MyTestCase)
mysuite = unittest.TestSuite([cases])
# 单独加上一条测试用例
# 如果调用的测试用例使用了ddt，则不能使用单独加入测试用例的方式了
mysuite.addTest(unittestrunner.MyTestCase('test_SearchChineseOK'))

myrunner = unittest.TextTestRunner(verbosity = 2)
myrunner.run(mysuite)
