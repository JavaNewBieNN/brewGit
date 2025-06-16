"""
json的写入
文件对象.write(字符串) 不能直接将python的列表字典作为参数传递
想要将python中的数据类型存为json文件，需要使用json提供的方法
不再使用 write

步骤：
1.导包 import json
2.写（w）方式打开文件
3.写入
json.dump(Python中的数据类型，文件对象)
"""

import json
my_list = [('admin', '123456', '登录成功'), ('root', '123456', '登录失败'), ('admin', '123123', '登录失败')]

with open('list_list.json', 'w', encoding='utf-8') as f:
    json.dump(my_list,f)
