"""
元组不能被修改(元组和列表的唯一的不同),允许重复元素存在

元组和列表一样都是可以封装多个不同类型的元素在内

"""

# 列表可以修改
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  # [100, 2, 3]

# 元组不能修改
my_tuple = (1, 2, 3)
#my_tuple[0] = 100  # 会报错:TypeError: 'tuple' object does not support item assignment


#定义元组
(1,2,3,4,5)
my_tuple = (1,2,3,4,5,"hello")

my_tuple_empty = ()
my_tuple_empty2 = tuple() #面向对象写法

t1 = (1,"hello",True)
t2 = ()
t3 = tuple()

print(f"t1的类型是:{type(t1)}, 内容是: {t1}")
print(f"t2的类型是:{type(t2)}, 内容是: {t2}") #t2的类型是:<class 'tuple'>, 内容是: ()
print(f"t3的类型是:{type(t3)}, 内容是: {t3}") #t3的类型是:<class 'tuple'>, 内容是: ()

# 定义单个元素的元素, 元组是(),列表是[], 只有单个元素必须写, 不然就是string类型
t4 = ("hello", )
print(f"t4的类型是:{type(t4)},内容是:{t4}") # t4的类型是:<class 'tuple'>,内容是:('hello',)

t4 = ("hello")
print(f"t4的类型是:{type(t4)},内容是:{t4}")  # t4的类型是:<class 'str'>,内容是:hello

# 元组的嵌套,数据可以是不同的数据类型
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是:{type(t5)}, 内容是: {t5}") #t5的类型是:<class 'tuple'>, 内容是: ((1, 2, 3), (4, 5, 6))

# 下标索引去取出内容
num = t5[1][2] # 6

# ----------------------元组的用法---------------------

# 1.index查找元素的index
t6 = ("itcast","python", "hello world")
index = t6.index("python")
print(f"在元组中t6的python的index是:{index}")

# 2.元组的操作:count统计方法
t7 = ("itcast", "heima","python", "java","c++", "c++")
num = t7.count("c++")
print(f"t8元组中的c++数量有:{num}个")

# 3. len统计元组的元素个数
t8 = ("itcast", "heima","python", "java","c++", "c++")
num = len(t8)

print(f"t8元组中的元素有:{num}个")


#------元组的遍历--------

index = 0
while index < len(t8):
    print(f"{t8[index]}")
    index += 1
    
for element in t8:
    print(f"{element}")


#------元组里面如果有一个list,拿这个list里面的元素是可以修改的---------

t9 = (1,2,["itcast","python"])
t9[2][0] = "黑马情侣"
t9[2][1] = "黑马"

print(f"t9的内容是:{t9}")
print(f"t9的内容是:{t9[2][0]}")






