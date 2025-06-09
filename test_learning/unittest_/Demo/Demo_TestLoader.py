"""
TestLoader和TestSuite的作用是一样的，对TestSuite功能的补充，用来组装测试用例的
比如：如果TestCase的代码文件有很多，（10， 20， 30）
    使用步骤：
    1.import
    2.实例化loader对象，并添加TestCase  ------------->得到的是suite对象
    3.实例化 runner
    4.runner执行suite对象
"""
#1.导包
import unittest


"""
2.实例化加载对象并添加TestCase
unittest.TestLoader().discover('TestCase所在的路径','TestCase的代码文件名')
TestCase所在的路径建议使用相对路径，TestCase的代码文件名可以使用*(任意多个任意字符)通配符
"""
suite = unittest.TestLoader().discover('./test_learning/unittest_/case','Demo*.py')
#suite = unittest.TestLoader().discover('./test_learning/unittest_/case','*Demo*.py')
#suite = unittest.TestLoader().discover('./test_learning/unittest_/case','*Demo*')
# 直接写名字也可以

#3.实例化runner
runner = unittest.TextTestRunner()

#4.run
runner.run(suite)

