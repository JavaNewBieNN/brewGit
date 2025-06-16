# b.py
import global_config
import a  # ❗必须引入 a 模块，让它初始化 shared（或者执行它的函数）
a.init()  # ✅ 主动执行初始化动作


print(global_config.shared["key"])  # 能访问到