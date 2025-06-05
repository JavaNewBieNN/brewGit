"""
代码的目的：学习 TestCase 模块的书写方法
"""
#1.导包
import unittest

#2.自定义测试类,需要继承 unittest 模块中的TestCase 类即可
class TestDemo(unittest.TestCase):
        #书写要求，测试方法必须以 test_开头 本质是 以 test开头
    def test_method1():
        print('测试方法1')

    def test_method2():
        print("测试方法2")

        
#3.书写测试方法



#4.执行用例（方法）






