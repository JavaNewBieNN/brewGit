"""
Fixture 测试夹具，是一种代码结构
在某些特定的情况下 会自动执行

method级别： 在每个测试方法（unit_tests case）执行前后都会自动调用的结构
            方法执行之前
        def setup(self):
            #每个测试方法执行之前都会执行
            pass

        def teardown(self):
            #每个测试方法执行之后都会执行
            pass

---------------------------------------------------------------------------------------------------

class级别： 在每个测试类中所有方法执行前后 都会自动调用的结构（在整个类中 执行之前执行之后 各一次）
            是一个类方法，类中所有方法之前
            如何定义一个类方法？
            @classmethod
            def setupClass(cls):
                pass

            @classmethod
            def teardownClass(cls):
                pass

---------------------------------------------------------------------------------------------------

module级别
模块：代码文件，在每个代码文件执行前后的代码结构

# 模块级别的需要写在类的外边直接定义函数即可
代码文件之前
        def setupModule():
            pass

代码文件之后
        def teardownModule():
            pass

方法级别和类级别的，前后的方法不需要同时出现，根据用例代码的需要自行的选择使用

"""
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        #每个测试方法执行之前都会先调用的方法
        print('输入网址.....')
    def tearDown(self):
        #每个测试方法执行之后都会调用的方法
        print('关闭当前页面.....')

    @classmethod                                #类名和对象都能调用，ClassName.f()    能被类直接调用
    def setUpClass(cls):
        print('1.打开浏览器')

    @classmethod
    def tearDownClass(cls):
        print('5.关闭浏览器')

    def test_1(self):
        print("输入正确用户名密码验证码，点击登录 1")

    def test_2(self):
        print("输入正确用户名密码验证码，点击登录 2")











"""
tools.py               ← 被测模块
test_tools.py          ← 写测试类 TestTools(TestCase)
    └── test_xxx()     ← 每个是测试“用例”
    └── setUp()        ← 用例前自动运行
    └── tearDown()     ← 用例后自动运行

suite = TestSuite()    ← 手动组合多个用例方法或类
loader = TestLoader()  ← 自动加载目录下所有 test_*.py
runner = TextTestRunner() ← 执行用例（无论是 suite 还是 loader.discover 返回的）

loader.discover('test_case', 'test_*.py') → 返回 suite → 用 runner 执行

----------------------------------------------------------------------------------------------------------

✅ 你的整体结构性理解（完全正确）
我们逐段来看：

1. TestCase 测试类：
✅ “自定义测试类继承了 TestCase，放在一个单独命名的模块里面，可以直接运行。”

完全正确，就是这么干的。命名一般是 test_xxx.py，类名 TestXxx(TestCase)。

2. 写 test_tools.py 来测 tools.py：
✅ “比如写了一个 tools.py 模块，我就写一个 test_tools.py，写一个 TestTools(TestCase) 来测试。”

非常标准的做法，这也是 小项目或模块单测的推荐结构。

3. Suite 用于组合多个测试方法或类：
✅ “suite 最核心的功能是组合多个测试类里的方法，比如 suite.addTest(className('methodName'))。”

这里你说得也对，只补充两个常用方式：
# 常规写法（推荐）
suite.addTests(loader.loadTestsFromTestCase(MyTestClass))

# 旧写法（已弃用）
suite.addTest(unittest.makeSuite(MyTestClass))

所以 suite 就是一个「可控的测试集合」，你可以按你的意图决定执行哪些测试。

4. Loader 是更大的组织方式，核心是 discover()：
✅ “loader 的核心是 discover()，它会加载多个模块，返回一个 suite。”

精确无误。通常写法如下：
loader = unittest.TestLoader()
suite = loader.discover(start_dir='test_case', pattern='test_*.py')
runner = unittest.TextTestRunner()
runner.run(suite)
你说得对：Loader 是服务于整个测试工程的“全自动加载器”。

5. Fixture 就是 setUp() 和 tearDown()：
✅ “没什么好说的，就是 setup 和 teardown。”

这个也对。不过我补充一点：

| Fixture 级别   | 方法                                              | 说明                          |
| ----------    | -----------------------------------------------   | ------------------- 
| 方法级         | `setUp()` / `tearDown()`                          | 每个 unit_tests\_xxx 方法前后执行     
| 类级           | `@classmethod setUpClass()` / `tearDownClass()`   | 整个类的所有测试前后只执行一次     
| 模块级         | `setUpModule()` / `tearDownModule()`              | 整个 py 文件的测试前后只执行一次  





"""




