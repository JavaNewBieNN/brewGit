"""
| 用途场景          | 最常见格式               |
| --------------- | --------------------    |
| API 返回值       | 最外层是字典（dict）      |
| 配置文件         | 最外层是字典（dict）      |
| 存储多条数据（日志、表格） | 最外层是列表（list），每个元素是字典 |


组成格式[(),(),()]
"""

import json
#C:/Users/NingNie/brewGit/pythonCodes/b_Notes/files/b.txt 参数可以是绝对路径
# open()
def read_data():
    with open("list_dict.json", encoding="utf-8") as f:
        data = json.load(f)  # l列表
        new_list = []
        for i in data:
            new_list.append((i.get("username"), i.get("password"), i.get("expect")))

    return new_list


print(read_data())
