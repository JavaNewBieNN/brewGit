"""
定义一个列表如 my_list = ["hello","python","itcast","hello"],练习对列表的增删改查统计的操作

1.增: 使用append()方法添加新的数据"heima"
2.删: 使用pop()方法删除第一个数据,使用remove()方法删除数据"hello"
3.改: 修改列表中的第一个数据为chuanzhi
4.查: 使用index()方法获取数据为"chuanzhi"的下标值,使用下标获取索引为2的数据
5.统计: 使用coung()方法统计列表中"hello"字符串的个数
6.统计列表中数据元素的个数(求列表的长度)

"""

my_list = ["hello","python","itcast","hello"]
my_list.append('heima')
print(my_list)
print("-" * 30)

my_list.pop()
my_list.remove('hello')
print(my_list)
print("-" * 30)

my_list[0] = 'chuanzhi'
print(my_list)
print("-" * 30)

index = my_list.index('chuanzhi')
print(index)
var = my_list[2]
print("-" * 30)

print(f"hello 有 {my_list.count('hello')}个")

print(f"列表的长度是: {len(my_list)}")




"""
# 通过input输入3个人的信息,每个人有姓名和年龄,将信息存入字典中,并将字典存入列表
# 遍历列表,打印每个人的信息,打印格式如下:
# 张三 20
# 李四 22
# 王五 23
列表的格式如下
[{'name':xx,'age':oo},{},{}]
"""


def info(dict):
    name = input('please input your name: ')
    age = input('please input your age: ')
    dict['name'] = name
    dict['age']  = age
    
info_list = list()

for i in range(3):
    info_dict = dict()
    info(info_dict)
    
    info_list.append(info_dict)
    
print(info_list)

for i in range(len(info_list)):
    temp_dict = info_list[i]
    
    print(f"{temp_dict.get('name')} {temp_dict.get('age')}")    
    

"""
有如下列表:
my_list = [{'id':1, 'money':10},{'id':2, 'money':20},{'id':3, 'money':30},{'id':4, 'money':40}]
要求:定义一个函数 func, 功能如下
    1.如果字典中 id 的值为奇数,则对money的值 + 20
    2.如果字典中 ID 的值为偶数,则对money的值 + 10
    3.打印输出列表,查看最终的结果

"""

my_list = [{'id':1, 'money':10},{'id':2, 'money':20},{'id':3, 'money':30},{'id':4, 'money':40}]

def func(my_list):
    
    for dicts in my_list:
        
        if dicts.get('id') % 2 != 0:
            dicts['money'] = dicts.get('money') + 20 #
        else:
            dicts['money'] = dicts.get('money') + 10
    
    print(my_list)
    
func(my_list)


"""
❌ 错误代码:
dict.get('money') = dict.get('money') + 20  # ❌    
Python 提示你:

	SyntaxError: cannot assign to function call

意思是:你不能给 dict.get('money') 这样的函数调用左边赋值.

❓1. 为什么这里不能用 dict.get('money') = dict.get('money') + 20?

因为 dict.get(...) 是一个函数调用的结果,Python 不允许你把结果当成左值(也就是不能对函数调用的结果做赋值).


✅ 正确写法:

你应该直接通过 [] 操作键值来修改字典的值:
dict['money'] = dict['money'] + 20
get() 只是安全读取用的,它不是设计来修改值的.

但如果你已经确定这个 key 一定存在,比如你刚刚创建的结构:
{'id':1, 'money':10}
就完全没必要用 .get(),直接用 d['money'] 更简单更快.



❓3. 我如果写 temp_dict = d,再改 temp_dict 会影响 my_list 吗?
答案是:

	✅ 会影响,因为 temp_dict = d 并没有复制数据,而是让 temp_dict 和 d 指向同一个字典对象.

来个例子感受一下:

d = {'money': 10}
temp_dict = d
temp_dict['money'] = 999
print(d)  # {'money': 999} ✅ 改变了原字典

temp_dict = d  # 是引用同一个对象

---------------------------------------------------------------
temp_dict = d 的底层内存机制

d = {'money': 10}
temp_dict = d

可以理解为:
	1.	d 是一个变量名,它本质上是个 引用(reference),指向某个字典对象的内存地址(比如内存地址 0x1234).
	2.	temp_dict = d 并不是"复制一个新对象",而是把这个地址(0x1234)复制给 temp_dict.
	3.	所以 temp_dict 和 d 是两个变量名,但它们指向同一个内存中的字典.
 
 变量名       ->  内存地址       ->  实际数据
d           ->  0x1234        ->  {'money': 10}
temp_dict   ->  0x1234        ->  {'money': 10}


🔄 二、那 .copy() 做了什么?
temp_dict = d.copy()
这时候发生了两件事:
	1.	创建了一个新的字典对象,内容是原始 d 的"浅复制".
	2.	新的对象有自己新的内存地址(比如 0x5678),但里面的 key 和 value 是从 d 拷贝过来的.

d           ->  0x1234        ->  {'money': 10}
temp_dict   ->  0x5678        ->  {'money': 10}  # 新字典,独立了



"""

# -------------------------------------------------------
"""

问题 1:dict.get(key) 拿到的是原始的 value 吗?是引用还是复制?

✅ 答案:是"引用"!不是复制!


d = {'data': [1, 2, 3]}
v = d.get('data')
v.append(4)
print(d)  # {'data': [1, 2, 3, 4]}


这说明:
	•	v = d.get('data') 并不会复制 [1, 2, 3],而是返回对这个 list 的引用(内存地址是同一个)
	•	所以修改 v,就等于修改了 d['data']

🧠 原因:

Python 中所有变量名都是引用(references),所以 get() 返回的 value 是"指向原字典里的 value 的指针",不新建对象.



❗️重要提醒:

但如果 value 是不可变类型(如 int, str, tuple),你修改返回值并不会影响原始字典:
d = {'x': 10}
v = d.get('x')
v += 1
print(d)  # {'x': 10} ✅ 原字典没变


"""




