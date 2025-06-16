import csv

"""
🔹2. os 是什么模块？
os 是 Python 的标准库模块之一，提供了跟操作系统交互的一系列功能，比如：

路径操作：拼接路径、拆分路径、获取当前文件路径等。

文件操作：查看文件夹是否存在、创建文件夹、删除文件、遍历文件夹。

环境变量操作：获取系统变量（比如 PATH）。

执行系统命令（比如 os.system()）。

我们现在用的 os.path 就是 os 模块里专门用于路径处理的子模块。
"""


def my_read():
    with open(r"/test_learning/pytest_/unit_tests\data.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)  # 会把 .csv 文件中的每一行 解析成一个字典（dict），键是列名，值是该行对应的字段。但是类型是class
        for row in reader:  # 每次你 for row in reader，它就返回一行数据对应的 dict，但它不是一次性加载整个文件到内存里的 list。
            print(row)  # 每一行是一个字典


def read_csv(filename):
    import os  # 写在函数里是合法的，Python 只会在调用函数时才执行这个 import（懒加载）。 有时用于减少模块加载时间、避免循环依赖，或者你只在一个函数中用到它，就可以这么写。
    """
    参数：一个字符串路径, 返回值：去掉最后的文件名部分，只保留文件夹路径
        os.path.dirname("C:/abc/def/file.py")  # 返回：C:/abc/def
    """
    base_path = os.path.dirname(__file__)  # 获取当前这个 .py 文件的所在文件夹路径, __file__ 是 Python 内置变量，表示当前这个脚本文件的完整路径

    r"""
    这个是为了拼出你要打开的文件的完整路径。
    os.path.join() 是用于拼接路径的函数，会根据操作系统自动使用正确的斜杠：
    Windows：\
    Linux/Mac：/
    
    os.path.join("C:/abc", "data.csv")
    # 返回：C:/abc/data.csv
    """
    full_path = os.path.join(base_path, filename)


    """
    newline='' 是什么意思？
    是为了让 Python 不自动转换换行符（\n, \r\n），
    特别是处理 CSV 文件时，不加这个可能一行读成两行，尤其在 Windows 上会出错。
    所以读 CSV 时加上 newline='' 是最佳实践。
    """
    with open(full_path, 'r', newline='') as f:
        reader = csv.reader(f) # 这个是 Python 标准库 csv 里的一个函数。作用：把 CSV 文件解析成一行一行的列表。
        return list(reader)[1:]


statement = read_csv("data.csv")

print(statement)  # [['1', '1', '2'], ['2', '3', '5'], ['3', '3', '6'], ['4', '4', '7']]
print(type(statement))  # <class 'list'>

r"""
name,age,city
Alice,23,Beijing
Bob,30,Shanghai

用 csv.DictReader(file) 读取后，你相当于得到了这样的结构:
[
  {'name': 'Alice', 'age': '23', 'city': 'Beijing'},
  {'name': 'Bob',   'age': '30', 'city': 'Shanghai'}
]

"""
