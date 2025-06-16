r"""
pytest在简单的基础上，对断言进行了高级封装（AST），对于python数据结构断言，非常友好
1.pytest实现了很多高级特性
2.鼓励大家积极使用assert
"""

r"""
3.练习
有函数 add 接收两个参数，并返回它们相加的结果
"""

import pytest
from file_reader import read_csv


def add(a, b):
    return a + b


def test_success():
    assert 1 == 1


@pytest.mark.xfail  # func, expected to be failed，xfailed
def test_failure():
    assert 1 == 2


class TestAdd:

    @pytest.mark.skip
    @pytest.mark.api
    def test_int(self):
        res = add(1, 3)
        assert res == 4

    @pytest.mark.skipif(1 == 2, reason="for demonstration") # wont skip
    @pytest.mark.web
    def test_str(self):
        res = add('1', '3')
        assert res == '13'

    @pytest.mark.xfail  # expected to be failed，but success，xpassed
    @pytest.mark.api
    def test_list(self):
        res = add([1], [2, 3, 4])
        assert (res == [1, 2, 3, 4])

    @pytest.mark.xfail  # expected to be failed, and actual failed, xfailed
    @pytest.mark.api
    def test_list1(self):
        res = add([1], [2, 3, 4])
        assert res == [1, 2, 3, 4, 5]


    r"""
    ✅ 什么是 Data-Driven Testing（数据驱动测试，DDT）？
    就是：测试逻辑是固定的，测试数据是从外部（CSV、Excel、数据库）读出来的，一份数据就是一组测试案例。
    你不用写 10 个 test_xxx 函数，而是用一组数据跑多组 case，非常适合做批量测试。
    
    @pytest.mark.parametrize("a,b,c", read_csv("data.csv"))
    意思是：把 read_csv("data.csv") 返回的内容，作为参数传给下面的测试函数。每一行数据（三个值）会对应 a, b, c 三个参数，生成一组测试 case。
    所以 parametrize("a,b,c", [...]) 的作用是：
    每次把其中一行分别赋值给 a, b, c 传入测试函数！
    
    这个字符串 "a,b,c" 是告诉 pytest：你测试函数有 3 个参数，分别叫 a、b、c，pytest 会自动拆分每一行数据映射到这 3 个参数上,等价于写成元组的形式：
    @pytest.mark.parametrize(("a", "b", "c"), [...])

    
    """
    @pytest.mark.ddt
    @pytest.mark.parametrize(
        "a,b,c",
        read_csv("data.csv")
    )
    def test_ddt(self, a, b, c):
        res = add(int(a), int(b))
        assert res == int(c), f"Expected {c}, got {res}"


r"""
C:\Users\NingNie\brewGit\pythonCodes\.venv\Scripts\python.exe                              解释器所在路径
C:\Users\NingNie\brewGit\pythonCodes\test_learning\pytest_\main.py                         被执行程序                        
============================= unit_tests session starts =============================             
platform win32 -- Python 3.11.8, pytest-8.4.0, pluggy-1.6.0                                 安装的系统软件版本
rootdir: C:\\Users\NingNie\brewGit\pythonCodes\test_learning\pytest_                         
collected 2 items                                                                           unit_tests case 数量

test_base.py .F                                                          [100%]

================================== FAILURES ===================================
________________________________ test_failure _________________________________

    def test_failure():
>       assert False
E       assert False

test_base.py:7: AssertionError
=========================== short unit_tests summary info ===========================
FAILED test_base.py::test_failure - assert False
========================= 1 failed, 1 passed in 0.05s =========================


"""
