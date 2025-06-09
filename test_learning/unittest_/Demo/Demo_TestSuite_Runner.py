"""
Test suite 就像你从中“挑几道题组成一个小测试卷”，你想测哪些，就选哪些，不一定全测。

为什么要用 test suite？
1.项目大了，不可能每次都跑所有测试（太慢）
2.某些模块还没写完、不稳定，不想影响其他测试
3.某些用例跑起来麻烦（依赖网络、数据库等）
4.做 smoke test、regression test 时，只测关键点

test suite 是把“要测的测试方法”集中组织起来
可以选定“测试类里的某些方法”而不是全测
它是你主动挑选构建的一套测试组合


"""

# 1.导包 unittest
import unittest

from Demo_TestCase import TestDemo1 # from module import Test_class
from Demo_TestCase2 import TestDemo2

# 2.实例化创建对象 套件对象，
suite = unittest.TestSuite()

# 3.使用套件对象添加TestCase
# 方式1 suite对象.addTest(testClass（‘方法名’）) 建议测试类名和方法名直接去复制，不要手写
suite.addTest(TestDemo1('test_method1_1'))
suite.addTest(TestDemo1('test_method1_2'))
suite.addTest(TestDemo2('test_method2_1'))
suite.addTest(TestDemo2('test_method2_2'))

# 方式2 将一个测试类中的所有方法进行添加
# suite.addTest(unittest.makeSuite(TestDemo1)) 已经弃用


# 4.实例化运行对象
runner = unittest.TextTestRunner()

# 5.使用运行对象去执行套件对象 runner.run(套件对象名字)
runner.run(suite)

