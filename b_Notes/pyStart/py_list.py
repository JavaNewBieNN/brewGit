name_list = ["a", "e", "i", "o", "u"]

"""
列表 list 
元组 tuple
字典 dictionary
集合 set
字符串 string
"""

# define
name = []
name1 = [1, 2, 3, 4]
listDiff = [1, 'python', "hello", 3.1415]  # 可以是不同的数据类型，支持嵌套
print(listDiff)

num1 = 1
num2 = 2
num3 = 3

name2 = [num1, num2, num3]

nameList = list()

print("--------------------------------------------------")
"""
1. 动态大小
Python 的列表是动态数组，这意味着列表可以在运行时自动扩展或缩小。当你向列表中添加或删除元素时，列表的大小会自动调整。
你可以随时向列表中添加新的元素，无需事先定义大小。
"""
my_list = [1, 2, 3]
my_list.append(4)  # 添加一个元素
print(my_list)  # 输出: [1, 2, 3, 4]

"""
2. 任意数据类型
list 可以存储任意类型的元素，包括数字、字符串、对象、甚至其他列表。
你可以在同一个列表中混合不同类型的数据。
"""
my_list = [1, "hello", 3.14, [1, 2, 3]]
print(my_list)  # 输出: [1, 'hello', 3.14, [1, 2, 3]]

"""
3. 可变性
列表是可变的，这意味着你可以改变列表的内容，比如添加、删除或修改元素。
"""
my_list = [1, 2, 3]
my_list[1] = 5  # 修改第二个元素
print(my_list)  # 输出: [1, 5, 3]

"""
4. 支持索引和切片
列表支持通过索引访问元素，索引从 0 开始。如果索引为负数，表示从列表的末尾开始计数。
你还可以对列表进行切片操作，获取子列表。
"""
my_list = [10, 20, 30, 40, 50]
print(my_list[2])  # 输出: 30
print(my_list[-1])  # 输出: 50
print(my_list[1:3])  # 输出: [20, 30]

"""
5. 包含重复元素
列表允许包含重复的元素，不像集合（set）必须包含唯一元素。
"""
my_list = [1, 2, 2, 3]
print(my_list)  # 输出: [1, 2, 2, 3]

"""
6. 支持内置函数和方法
列表有许多内置的函数和方法可以使用，如 append()、extend()、insert()、remove()、pop() 等。
"""
my_list = [1, 2, 3]
my_list.append(4)  # 添加元素 4
my_list.remove(2)  # 移除元素 2
print(my_list)  # 输出: [1, 3, 4]

"""
7. 支持迭代
列表是可迭代的，你可以使用 for 循环来遍历列表中的所有元素。
"""
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

"""
内存管理
Python 的 list 中，每个元素的引用存储在一个连续的内存块中。这个数组存储的是指向对象的指针，而不是对象本身。
这意味着 Python 的 list 可以存储任何类型的对象，包括混合类型。

解释：
例如，你的 list = [1, "hello", 3.14] 中存储的是指向整数、字符串和浮点数对象的指针。
由于 list 只存储对象的引用，而不是对象本身，这使得 Python 的 list 可以灵活处理任意类型的数据。
"""
print("-------------------------------------------------------------------------")
"""
list常用操作
list对象.index(元素)
"""
mylist = ["a", "e", "i", "o", "u"]
index = mylist.index("a")
print(f"a's index is {index}")
# index1 = mylist.index("p")  # ValueError: 'p' is not in list



