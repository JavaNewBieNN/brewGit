"""
代码的目的：学习 TestCase 模块的书写方法
所有test case必须写在测试类中，并且以test_开头
"""
#1.导包
import unittest

#2.自定义测试类,需要继承 unittest 模块中的TestCase 类即可
class TestDemo1(unittest.TestCase): #自己定义的测试类，继承TestCase类，unittest是一个包

# 3.书写测试方法，即 用例代码 #书写要求，测试方法必须以 test_开头 本质是 以 test开头
    def test_method1_1(self):
        print('测试方法1——1')

    def test_method1_2(self):
        print("测试方法1——2")




