"""
1.创建函数
2.添加装饰器
3.添加 yield 关键字

"""
from datetime import datetime

import pytest


def test_1(f):  # 第一种使用fixture的方式，这种方法能够拿到 yield 返回的参数
    print(f)
    pass


@pytest.mark.usefixtures("f")  # 第二种使用fixture的方式
def test_2():
    # ❗如果你用 @pytest.mark.usefixtures("f")，就不能用 yield 123 的值 python
    pass


r"""

在测试中 yield最典型的案列：
✅ 最典型的用法示例：打开数据库连接
@pytest.fixture
def db_conn():
    conn = connect_to_db()
    yield conn   # 👈 把连接对象传给测试函数
    conn.close()

def test_query(db_conn):
    result = db_conn.query("SELECT * FROM users")
    assert len(result) > 0


db_conn 是 fixture 名，也是测试函数参数名
conn 是连接对象，通过 yield 传给测试函数
测试函数里可以直接用 db_conn 做查询等操作

"""

""" 
| `scope`      | 含义               | 生命周期（多久创建/销毁一次）         | 应用场景举例               |
| ------------ | ---------------- | ----------------------- | --------- |
| `'function'` | 每个测试函数一次（默认）     | 每次 `test_xxx()` 都会执行一遍  | 数据隔离最好            |
| `'class'`    | 每个测试类一次          | 执行这个类中所有方法前运行一次         | 类共享资源            |
| `'module'`   | 每个 `.py` 文件一次    | 模块中所有测试函数运行前后各执行一次      | 数据库连接        
| `'session'`  | 整个测试会话一次         | pytest 执行期间只创建一次，所有测试共用 | 登录认证、全局缓存    |
| `'package'`  | 每个包一次（pytest 7+） | 每个测试包初始化一次（较少使用）        | 跨模块资源共享        |
"""
