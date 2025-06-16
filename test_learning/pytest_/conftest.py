
r"""
pytest.ini
conftest.py  都建议放在根目录 pytest在运行的时候会先去找这两个东西 pytest.ini---> conftest.py--->unit_tests case


conftest就是 为了全局范围全局共享的 fixture
两个条件必须满足： 1. scope = 'session'
                2. 必须放在conftest
"""
from datetime import datetime

import pytest


@pytest.fixture(scope='session')
def ff():
    print("我也是fixture，但是被fixture使用")

r"""
1.yield 后面的值可以是任意类型, 可以 yield 出 任何 Python 对象，pytest 会把它作为返回值，传给需要它的测试函数。
2.测试函数 test_1(f) 里的 f 是什么？
    这里的 f 是： pytest 自动注入的参数，名字对应于你注册的 fixture 函数名（f），值就是 yield 出来的那个值。
    test_1(f) 不是你自己传参，是 pytest 执行时自动帮你注入的
    pytest 看你写了 f 参数，就去找有没有一个叫 f 的 fixture
    找到 @pytest.fixture def f(): 后，执行它，取 yield 的返回值
    把这个值注入到 test_1(f) 中

3.那 f 是 fixture 的“引用”还是 yield 的值？
    结论很明确：是 yield 的值本身，不是 fixture 的引用，也不是函数。

4. 测试函数可以不接收 yield 的值吗？
    可以
    用marker
    只是声明用这个 fixture，但你并不关心它返回什么。常用于只做 setup/teardown 的情况，比如：

    打开数据库连接 → 不需要在测试里用

    启动服务 / 初始化环境 → 不需要在函数中访问值

"""


@pytest.fixture(autouse=True,
                scope='session')  # 🔹 1. autouse=True 的作用：不需要在测试函数里传入 fixture 参数名，这个 fixture 就会被自动调用。所有能被 scope=... 命中的 unit_tests case 都会自动触发 fixture
def f(ff):  # pytest -s   ff会先被执行
    print(datetime.now(), "unit_tests case start to execute ")
    # before
    yield 123  # 开始执行 unit_tests case    只能有一个, 这里是个generator，会产生123这个份值
    # after
    print(datetime.now(), "unit_tests case f one")
