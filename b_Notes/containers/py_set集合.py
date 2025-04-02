"""
集合的特点:
1:没有重复元素
2:无序,没有index
3.允许修改
"""

"""
列表    list    []
元组    tuple   ()
字符串  string   ""
集合    set     {}
"""

#定义一个集合  {}
my_set = {"itcast", "itheima", "hello world", "python","itcast", "itheima", "hello world", "python","黑马情侣"}
print(f"my_set的内容是:{my_set},类型是{type(my_set)}")#{'hello world', 'itcast', 'python', 'itheima'},类型是<class 'set'> 自动去重

#定义空集合
my_set_empty = set()
print(f"my_set的内容是:{my_set_empty},类型是{type(my_set_empty)}") # set(),类型是<class 'set'>

#添加新元素
my_set.add("python")
my_set.add("itcast")
print(f"my_set添加元素后结果是:{my_set}")

#移除元素
my_set.remove("黑马情侣")
print(f"my_set移除黑马情侣以后结果是: {my_set}")


#随即取出一个元素pop   element = list.pop(index)
my_set = {"a","b","c","d"} 
element = my_set.pop()
print(f"被取出的元素是{element},剩下的列表是:{my_set}") #每次被弹出的都可能不一样

#清空集合 clear
my_set.clear()
print(f"集合备清空了,结果是:{my_set}")

#取两个集合的difference,结果返回一个新集合(set1有,但是set2没有的),但是set1,set2不变
set1 = {1,2,3}
set2 = {1,5,6}

set3 = set1.difference(set2)
print(f"取出差集合后的结果是:{set3}") # {2,3}
print(f"set1:{set1}")
print(f"set2:{set2}")

#消除两个集合的difference,在set1内删除和set2相同的元素,set1被修改,set2不变
#grammar: set1.difference_update(set2)
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference_update(set2)

print(f"difference update后: {set1},set3是{set3}")


#两个sets 合并成1个,union,原来的集合元素不变,会得到一个新的集合
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2) # 12356
print(f"2集合合并结果:{set3}")
print(f"合并后集合1:{set1}")
print(f"合并后集合2:{set2}")

# 统计集合的元素数量
set1 = {1,2,3,4,5,5,4,3,2,1}
num = len(set1)
print(f"集合内的元素数量有:{num}个") # 5 

#集合的遍历,只能用for循环
"""
集合不支持下标索引,不能用while循环,while循环的思路,每次把index所在的元素取出来,然后打印出来,index更新+=或者-=,移动到下一个index,但是这必须是有index操作才行
# ---------------列表的循环---------------
def list_while_func():
    my_list = ["黑马情侣","白马情侣","绿马情侣"]

    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"{element} ", end="")
        index += 1
    
"""

set1 = {1,2,3,4,5}

for i in set1:
    print(f"{i}")
    
    
"""
set本身确实不是设计来"随机取出"或"按顺序取值"的容器.它的设计初衷是用来做:
1.去重
2.判断成员是否存在(in 操作很快)
3.集合操作(交集、并集、差集)
"""
s = {'apple', 'banana', 'cherry'}

if 'apple' in s:
    s.remove('apple')  # 从 set 中删掉
    element = 'apple'  # 保存到变量中
    print("Got:", element)


#
s = {'apple', 'banana', 'cherry'}

# 注意:我们不想动原来的 set
for element in s:
    print("Do something with:", element)
    break  # 只处理一个



#----------------小练习-----------------
print(f"------------------------------")

"""
有如下列表对象:
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客''itheima','itcast','itheima','itcast','best']
请定义一个空集合
在for循环中将列表的元素添加至集合
最终得到元素去重后的集合对象,并打印输出
"""
#请定义一个空集合
set_empty = set()
#在for循环中将列表的元素添加至集合
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
for element in my_list:
    set_empty.add(element)

#最终得到元素去重后的集合对象,并打印输出

for element in set_empty:
    print(f"{element} ", end = '')