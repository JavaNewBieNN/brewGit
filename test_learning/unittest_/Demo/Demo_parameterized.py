"""
参数化代码
1.导包 unittest/parameterized
2.定义测试类
3.书写测试方法（用到的测试数据使用变量替代）
4.组织测试数据并且传参

"""
import json

# 组织测试数据 [(),(),()] or [[],[],[]], 数据和参数一定要保持一致，列表中有几组数据，就是几个用例，顺序一定和test case里面的数据顺序保持一致
# data = [
#     ('admin', '123456', '登录成功'),
#     ('root', '123456', '登录失败'),
#     ('admin', '123456123123', '登录失败')
# ]

# 1.导包 unittest/parameterized
import unittest
from parameterized import parameterized  # 从 parameterized模块导入这个parameterized函数
from test_learning.unittest_.case import Demo_TestCase3  # 导入整个模块


def build_data():
    with open('data.json', encoding='utf-8') as f:
        result = json.load(f) # [{},{},{}]
        data = []
        for i in result: # {}
            data.append((i.get('username'), i.get('password'), i.get('expect')))
            #(i.get('username'), i.get('password'), i.get('expect')) # 变成元组
    return data # 返回成列表 # [(),(),()]


# 2.定义测试类
class TestLogin(unittest.TestCase):

    # 3.书写测试方法（用到的测试数据使用变量替代）
    @parameterized.expand(build_data()) # 上面函数作为参数传入进来
    def test_login(self, username, password, expect):
        self.assertEqual(expect, Demo_TestCase3.login(username, password))
