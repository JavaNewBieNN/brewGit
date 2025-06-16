r"""
生成器函数是一个可以多次暂停和恢复执行的函数，每次 yield 会“生成”一个值，而不是一次性返回所有结果。

它不是一次性执行完、返回结果、退出，而是一步一步来，每次产生一个值（yield），直到结束。
🧠 类比帮助理解：
📦 普通函数（return）像快递打包一次性全发：

def get_numbers():
    return [1, 2, 3]  # 一次性把所有东西打包好返回

print(normal())  # 输出：[1, 2, 3]

特点：
    调用一次就结束了
    函数内部运行完了
    所有结果一下子返回了（内存占用高）


🚚 生成器函数（yield）像快递一件件送：
def get_numbers():
    yield 1
    yield 2
    yield 3

g = get_numbers()
print(next(g))  # 输出 1
print(next(g))  # 输出 2
print(next(g))  # 输出 3

每次调用 next()，送一件
上次暂停的地方继续执行
内存占用少、效率高，尤其适合大数据、懒加载


✅ 用在哪里最常见？
| 场景                 | 为什么用生成器（yield）        |
| ------------------ | --------------------- |
| **读取大文件**          | 一行行 yield，节省内存        |
| **惰性计算**           | 不急着算出所有数据             |
| **自定义迭代器**         | `for x in ...` 背后原理   |
| **pytest fixture** | 分开执行 setup 和 teardown |


✅ 总结对比表：
| 特性   | 普通函数 (`return`) | 生成器函数 (`yield`)               |
| ---- | --------------- | ----------------------------- |
| 返回   | 一次性返回整个结果       | 每次暂停，按需返回一个值                  |
| 内存占用 | 高               | 低，逐步生成                        |
| 控制权  | 函数结束后彻底返回       | 控制权可以中断后恢复                    |
| 使用方式 | 直接调用，返回值        | 返回 generator 对象，用 `next()` 取值 |



"""

def count_up():
    yield 1 # 执行到这里立马就不执行了，不会执行下一行的 print
    print("执行了第1个yield，但是还没执行完呢！")

    yield 2
    print("执行了第2个yield，但是还没执行完呢！")

    yield 3
    print("执行了第3个yield，func终于执行完了！")

# for i in count_up():
#     print(i)

g = count_up()
print(next(g))  # next() 是 Python 内置函数，用于从迭代器（iterator）中取下一个值。 # 输出 1（执行到第一个 yield）
print("-" * 30)
print(next(g))      # 输出 2（继续执行到下一个 yield）
print("-" * 30)
print(next(g))      # 输出 3（再继续）

