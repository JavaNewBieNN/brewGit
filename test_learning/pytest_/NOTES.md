# test case 结果缩写

| 缩写 | eng     | meaning       |
|----|---------|---------------|
| .  | passed  | 通过            |
| F  | failed  | fail          |
| E  | error   | fixture执行报错   |
| s  | skipped | 跳过            |
| X  | xpassed | 预期外的通过（不符合预期） |
| x  | xfailed | 预期内的失败（符合预期）  |

---
# 1. test case 规则

### test case discover 规则
#### 测试框架在识别，load test case的过程称之为 test discover 用例发现
#### pytest的用例发现步骤：
- 1.遍历所有目录，例外.venv, .开头的目录比如.DS_Store哥们是hidden文件
- 2.打开python文件， test_*.py 或 *_test.py 结尾
- 3.遍历所有的Test开头类
- 4.收集所有的test_开头的 函数（放在类中） 或者 方法

# 2. test case 内容规则
#### pytest 8.4增加了一个强制要求
### pytest对test case的要求
- 1.可调用的（func，method，class，obj）
- 2.名字test_开头
- 3.没有参数(参数有另外含义)
- 4.没有返回值（默认为None）
---

# 3.配置框架
### 配置可以改变pytest默认的规则
### 常用参数
    -v： 增加详细程度
    -s： 停止io捕获，在test case中正常的使用输入和输出
    -x： 快速退出，当遇到有一个test case失败那么就立刻停止    
    -m： test case的筛选    pytest -m label_name 只执行该label的test case
    -vs  verbose模式 更详细的测试过程 主要是fixture的使用情况
    pytest -vv pytest -s
----

# 4. pytest 默认 test case的规则，以及应用基础
1. module名字必须以test_开头或者_test结尾  
2. 测试类必须以Test开头  
3. 测试方法必须以test开头

---


# 5. pytest test case 的运行方式
1. 主函数模式：  
     - 运行所有： pytest.main()
     - 指定模块： pytest.main([-vs test_login.py]) 
   
2. cli模式：  
     - 运行所有：pytest
     - 指定模块 pytest -vs test_login.py

### pytest <路径>/<文件名>::<函数名>
        -pytest a/a1/a1_1.py::test_a
        -路径必须是相对你当前目录的。

### 对于框架来说，没有异常就是pass，有就是fail
def test_a():  
    1/0        这会引发异常，所以会失败

def test_a():
    pass        这永远会测试通过


---
# 6.标记mark
#### 标记可以让testcase 与众不同，进而可以被区别对待 用pytest.ini实现
### 1.用户自定义标记 
        1.先注册
        2.再标记  # 只能实现test case筛选
        3.后筛选
### 2.pytest框架内置标记
#### 用户自定义标记 用test case 增加特殊执行效果
#### 和用户自定义标记的区别
    1.无需注册，可以直接使用
    2.不仅可以筛选，还可以增加效果
    3.不同的标记能够增加不同的特殊效果
        skip：无条件跳过
        skipif：有条件跳过
        xfail：预期失败
        parametrize：参数化
        usefixtures：使用fixtures
#### 数据驱动测试 = 参数化测试 + 数据文件
#### 根据数据文件的内容，动态决定test case的数量和内容

---
# 7.数据驱动测试参数 (项目更多的使用)
### 1.首先用一个数据容器装 csv 或者 json之类的
### 2.写一个函数读取这个 容器中的数据, 一般 返回一个tuple/list 等数据容器的 class
### 3."a,b,c" 参数化读取 映射到 读取文件的函数，再把a,b,c放到 test case 的参数中

---

# 8. Fixture夹具
### 在test case 执行之前之后自动运行的代码块
### 场景：
    before 加密参数  / after：解密结果
    before 启动浏览器  / after：关闭浏览器
    before 登录注册账号  / after：删除账号

### 1.创建fixture
        1.创建函数
        2.添加装饰器@pytest.fixture
        3.添加yield关键字

### 2.使用fixture 2 种 使用方式
    1.在test case的参数列表中，加入fixture的名字即可
    2.给test case加上 usefixtures 标记 @pytest.mark.usefixtures("fixture_name")
        一般不用标记，因为如果类中的基本上大多数method都要测试，那么最好就是直接传参就好了
        因为标记是这个method / test case 单独拿出来跑一般

### 3.高级用法
    1.自动使用
    2.依赖使用
    3.返回内容：接口自动化封装：接口关联
    4.范围共享：
        - 默认范围是：function
        - 全局共享：session 
                - 使用 conftests.py

---
# 9.plugin 插件管理
#### pytest插件生态是pytest特别的优势之处

### 插件分成两类
- 内置插件 不需要安装
- 第三方插件 需要安装

### 插件的启用管理：
- 启用 -p
- 禁用 -p no:    pytest --html=report.html -p no:html

### 插件的使用方式：
    1.参数
    2.配置文件

    3.fixture  这两个主要是为了test case来使用的
    4.mark

---
# 10. 常用的第三方插件
#### 1. pytest-html
        用途：生成HTML测试报告
        安装：pip install pytest-html
        使用 pytest --html=report.html --self-contained-html

#### 2.pytest-xdist 分布式执行
        安装： pip install pytest-xdist
        使用： -n N N表示用几个多进程的分布式 来执行
        只有在任务本身耗时时间较长，超出调度成本很多的时候，才有意义
        分布式执行，有并发问题，有资源的竞争，有乱序

#### 3.pytest-rerunfailures
        用途：用例失败之后，重新执行 ui测试，网络波动之类的
        安装：pip install pytest-rerunfailures
        使用：--reruns N --reruns-delay 1  不要在短时间做重复操作   最多N次运行不算第1次 第2个参数多久再重复1次


#### 4. pytest-result-log
        用途：把test case的执行结果记录到日志文件中
        安装：pip install pytest-result-log
        使用：在pytest.ini里面添加，不使用命令行参数

---
# 11.企业级测试报告
#### allure 是一个测试报告框架
        安装：pip install allure-pytest
        配置：addopts == --alluredir=temp --clean-alluredir

        生成报告：allure generate -o report  -c temps    
        这个命令会在current folder 建立一个report folder

#### allure 支持对于test case进行分组和关联 (敏捷开发术语)
@allure.epic    史诗  项目<br>
@allure.feature 主题  模块<br>
@allure.story   故事  功能<br>
@allure.title   标题  用例<br>

使用相同装饰器的test case，自动并入一组<br>

---
# 12. 封装测试框架
#### pytest是通用型测试框架，很像unittest但是更加强大，可以扩展
#### 在pytest的基础上，结合业务需求封装
    接口自动化测试框架
    web自动化测试框架
    App自动化测试框架

### 框架应该拥有什么？
#### 1.日志文件 
        pytest.ini 里面进行配置可以

### 2. 统一执行文件
        
### 接口封装
    pytest + yaml + requests + allure + logging接口自动化测试框架
    


---
# 14. YAML文件格式
一句话：YAML 完全兼容JSON格式，并且支持 Python相似写法<br>
重点：<br>
    1.yaml 完全兼容 JSON  
    2.是数据格式，不是编程语言  
    3.像python一样容易编辑和阅读  

### 1.安装 yaml module  
    pip install pyyaml

### 2.编写yaml文件
    1. #作为注释符
    2.使用intent 2两个空格
    3.成员表示：  
        - 表示list成员
        - 表示dict 成员
    4.兜底 完全兼容JSON

### 3.加载 yaml文件

# 15.接口测试 test case
### 1.设计test case内容
#### 1.名字  
#### 2.mark （可选）
#### 3.步骤    
    1.请求接口: GET http://www.google.com
    2.响应断言: status_code == 200
    3.提取变量: json()['code'] 

### 2.YAML 表示test case
---

# 16. 封装接口自动化框架
### 1.请求接口
    外部工具 request
    
    从HTTP协议抓包角度，请求由3部分组成
        - 行： 方法+地址（必填）
        - 头： 请求头（键值对）
        - 体： 参数内容



### 2.断言响应

















        











