import yaml # import yaml 是导入了 PyYAML 这个库的主模块 yaml。

def load_yaml(path):
    """
    safe_load 是比 load 更安全的版本
    它只能加载基本类型（比如 dict、list、int、float、str）
    避免了 load() 函数中可能执行任意 Python 对象的安全风险（比如反序列化对象时执行代码）
    """
    with open(path, 'r', encoding="utf-8") as f:
        s = f.read()
        data = yaml.safe_load(s) # 把一个 YAML 格式的字符串 s 解析成 Python 中对应的数据结构（dict、list 等）
        print(data)

    return data

print(load_yaml("ning.yaml"))