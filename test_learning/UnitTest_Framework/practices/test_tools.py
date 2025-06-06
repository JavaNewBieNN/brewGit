"""
1.在tools模块中定义add函数，对两个数字进行求和计算
2.书写 TestCase 代码对 add()进行测试
TestCase 1: 1, 2     3
TestCase 2: 10,20    30
TestCase 3: 2,3      5
"""

import unittest
from tools import add

class TestTools(unittest.TestCase):

    def test_add1(self):
        if add(1,2) == 3:
            print("测试通过")
        else:
            print('测试失败')

    def test_add2(self):
            if add(10,20) == 30:
                print("测试通过")
            else:
                print('测试失败')

    def test_add3(self):
            if add(3,2) == 5:
                print("测试通过")
            else:
                print('测试失败')

