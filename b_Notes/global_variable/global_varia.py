"""
✅ 一句话核心结论： Python 中的“全局变量”是“模块级全局”，不是“程序级全局”。

✅ 什么是“模块级全局”？ 在 Python 里，每个 .py 文件就是一个模块（module）。你在某个模块里定义的变量：

# file: my_module.py
x = 42  # 模块级全局变量

这个 x 是这个模块里的“全局变量”，它的作用范围是： 在这个 .py 文件中全局可用      在别的模块中不是自动可见的，除非你专门 import

🧠 举个例子帮你搞清楚：
config.py
x = 100

main.py
from config import x

print(x)  # 输出 100
x = 200   # 修改的是 main.py 里的 x，不会影响 config.py

config.py 中的 x 是那个模块的“全局变量" 在 main.py 中引入后 会被复制一份进来 模块之间的变量不共用作用域，除非你传递、导入


"""