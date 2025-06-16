"""
断言 assert： 让程序代替人工自动的判断预期结果和实际结果是否相符

断言的结果有两种:
> True, unit_tests case 通过
> False, unit_tests case 失败
--------------------------------------------
常用的UnitTest断言方法

self.assertEqual(expected_value, actual_value)

assertIn(expected_value, actual_value) #判断预期结果是否包含在实际结果中，包含通过，不包含，unit_tests case fail throw  exception

assertIn('admin','admin')
assertIn('admin','adminnn')
assertIn('admin','aaaaadmin')
assertIn('admin','aaaaadminnnnnn') 是
assertIn('admin','addddmin') 不是

在unittest中使用断言，都需要通过self.断言方法 来验证
--------------------------------------------------------------------------------------------

工作场景：
1.测试数据一般在json文件中
2.使用代码读取json文件，提取我们想要的数据----->[(),(),()] or [[],[],[]]   这里说的是，我们传参要传入这样的参数才行

安装插件：
unittest 框架本身是不支持   参数化的，要使用参数化，需要安装插件来完成
安装：
- 联网安装（在cmd窗口安装）
pip install parameterized
pip是python中包（插件）的管理工具，这个工具下载安装插件
-------
验证：
pip list #查看到 parameterized

新建一个 python 代码文件 导包验证
from pa... import pa...
--------------------------


"""

import unittest

# from test_learning.unittest_.case.Demo_TestCase3 import login # 只导入一个方法 login可以直接用那样
from test_learning.unittest_.case import Demo_TestCase3 # 导入整个模块


class TestLogin(unittest.TestCase):

    def test_username_password_success(self):
        # "正确的用户名和密码：admin，123456，登录成功"， 可以是任何类型，但是class需要实现__eq__方法
        self.assertEqual('登录成功',Demo_TestCase3.login('admin','123456')) #


    def test_username_password_fail(self):
        self.assertEqual('登录失败',Demo_TestCase3.login('something else than admin','something else than 123456'))




    def setUp(self):
        #每个测试方法执行之前都会先调用的方法
        print('输入网址.....')
    def tearDown(self):
        #每个测试方法执行之后都会调用的方法
        print('关闭当前页面.....')

    @classmethod                      #类名和对象都能调用，ClassName.f()    能被类直接调用
    def setUpClass(cls):
        print('1.打开浏览器')

    @classmethod
    def tearDownClass(cls):
        print('5.关闭浏览器')

    def test_1(self):
        print("输入正确用户名密码验证码，点击登录 1")

    def test_2(self):
        print("输入正确用户名密码验证码，点击登录 2")
