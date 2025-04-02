name_list = ["a", "e", "i", "o", "u"]

"""
# 基本语法
【元素1,元素2,元素3,元素4,...】

# 定义变量
变量名称 = 【元素1,元素2,元素3,元素4,...】

# 定义空列表
变量名称 = 【】
变量名称 = list()

"""

# define
name = []
name1 = [1, 2, 3, 4]
listDiff = [1, 'python', "hello", 3.1415]  # 可以是不同的数据类型,支持嵌套
print(listDiff)

num1 = 1
num2 = 2
num3 = 3

name2 = [num1, num2, num3]

nameList = list()

print("--------------------------------------------------")
"""
1. 动态大小
Python 的列表是动态数组,这意味着列表可以在运行时自动扩展或缩小.当你向列表中添加或删除元素时,列表的大小会自动调整.
你可以随时向列表中添加新的元素,无需事先定义大小.
"""
my_list = [1, 2, 3]
my_list.append(4)  # 添加一个元素
print(my_list)  # 输出: [1, 2, 3, 4]

"""
2. 任意数据类型
list 可以存储任意类型的元素,包括数字、字符串、对象、甚至其他列表.
你可以在同一个列表中混合不同类型的数据.
"""
my_list = [1, "hello", 3.14, [1, 2, 3]]
print(my_list)  # 输出: [1, 'hello', 3.14, [1, 2, 3]]
"""
3. 可变性
列表是可变的,这意味着你可以改变列表的内容,比如添加、删除或修改元素.
"""
my_list = [1, 2, 3]
my_list[1] = 5  # 修改第二个元素
print(my_list)  # 输出: [1, 5, 3]

"""
4. 支持索引和切片
列表支持通过索引访问元素,索引从 0 开始.如果索引为负数,表示从列表的末尾开始计数.
你还可以对列表进行切片操作,获取子列表.
"""
my_list = [10, 20, 30, 40, 50]
print(my_list[2])  # 输出: 30
print(my_list[-1])  # 输出: 50
print(my_list[1:3])  # 输出: [20, 30]

"""
5. 包含重复元素
列表允许包含重复的元素,不像集合(set)必须包含唯一元素.
"""
my_list = [1, 2, 2, 3]
print(my_list)  # 输出: [1, 2, 2, 3]

"""
6. 支持内置函数和方法
列表有许多内置的函数和方法可以使用,如 append()、extend()、insert()、remove()、pop() 等.
"""
my_list = [1, 2, 3]
my_list.append(4)  # 添加元素 4
my_list.remove(2)  # 移除元素 2
print(my_list)  # 输出: [1, 3, 4]

"""
7. 支持迭代
列表是可迭代的,你可以使用 for 循环来遍历列表中的所有元素.
"""
my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)

"""
内存管理
Python 的 list 中,每个元素的引用存储在一个连续的内存块中.这个数组存储的是指向对象的指针,而不是对象本身.
这意味着 Python 的 list 可以存储任何类型的对象,包括混合类型.

解释:
例如,你的 list = [1, "hello", 3.14] 中存储的是指向整数、字符串和浮点数对象的指针.
由于 list 只存储对象的引用,而不是对象本身,这使得 Python 的 list 可以灵活处理任意类型的数据.
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



# -------------------list常用操作------------------------
myList = ["itcast","itheima","python"]

# 1.1 查找某元素在列表中的下标索引
index = myList.index("itheima") # 0

print(f"列表是: {myList}")
# 1.2 如果查找的元素不存在会报错
# index = myList("hello") 

# 2 修改特定位置(索引)的元素值   list【index】 = value
myList[0] = "czjy"
print(f"修改过后的结果是: {myList}")

# 3. 指定位置插入新元素
myList.insert(1,"best")
print(f"插入过后的元素是: {myList}")

# 4. 尾部添加新的元素
myList.append("黑马情侣")
print(f"append过后的元素是: {myList}")

# 5 增加一批元素 list.extend(list2)
myList2 = [1,2,3]
myList.extend(myList2)
print(f"追加新列表之后的列表: {myList}")

# 6 删除元素 
# del list[index]
mylist = ["itcast","itheima","python"]

del mylist[2]
print(f"删除元素是: {mylist}") # ['itcast', 'itheima']

# 6.2 list.pop(index)
mylist = ["itcast","itheima","python"]
element = mylist.pop(2)  #pop可以接收,del只能删除

print(f"删除的元素是: {element}, 删除后的列表是{mylist}") # python, ['itcast', 'itheima']


# 7 删除某元素在列表中的第一个匹配项
mylist = ["itcast","itheima","itcast","itheima","python"]
mylist.remove("itheima")
print(f"通过remove方法一处元素后,列表的结果是:{mylist}") # ['itcast', 'itcast', 'itheima', 'python']

# 8 清空列表
mylist.clear()
print(f"列表被清空了,结果是:{mylist}")

# 9 统计某元素在列表内的数量 list.count("element")
mylist = ["itcast","itheima","itcast","itheima","python"]
count = mylist.count("itcast")
print(f"itcast有{count}个")

# 10 统计元素总共有多少个
count = len(mylist)
print(f"列表的元素数量总共有:{count}个")








# ---------------列表的循环---------------
def list_while_func():
    my_list = ["黑马情侣","白马情侣","绿马情侣"]

    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"{element} ", end="")
        index += 1
    
    
def list_for_func():
    
    mylist = [1,2,3,4,5]
    for element in my_list:
        print(f"列表的元素有:{element} ")    



list_while_func()
print()
list_for_func()


"""
#-------练习---------
列表 【21,25,21,23,22,20}代表学生年龄
1:定义列表,并用变量接收它
2:追加一个数字31,到列表尾部
3:追加一个新列表【29,33,30】到列表尾部
4:取出第一个元素(21)
5:取出最后一个元素(30)
6:查找元素31,在列表中的下标位置
"""
print("---------------------------------------")



mylist = [21,25,21,23,22,20]
mylist.append(31)
print(f"{mylist}")

mylist.extend([29,33,30])
print(f"{mylist}")

#element = mylist.pop(0) 单纯拿到该元素不需要pop
print(f"element is : {element}, list is : {mylist}")

#element = mylist.pop(-1) 单纯拿到该元素不需要pop
print(f"element is : {element}, list is : {mylist}")

element = mylist.index(31)
print(f"index is : {element}, list is : {mylist}")





