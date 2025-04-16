"""
key:value
适用场景:通过一个东西检索到另一个东西
通过key找到value

姓名                成绩
王力宏              77
周杰伦              88
林俊杰              99

定义:
set:   {e1,e2,e3,...}
dict:  {key:value, key:value, key:value, ......}
key就是表示数据的名字,value就是具体的数据
变量 = {
    名字1:值1,
    名字2:值2,
    名字3:值3,
    }
    
特点:key是唯一的不能重复的,value可以是任意数据
    key一般是字符串表示,可以是数字,不能是列表
"""
#定义字面量
{"王力宏":99,"周杰伦":88,"林俊杰":77}

#定义空字典
my_dict = {}
print(f"my_dict的类型是: {type(my_dict)}")

#使用 类实例化定义
my_dict = dict()
print(type(my_dict),my_dict) # <class 'dict' >{}

#非空字典

my_dict2 = {"name": "小明", "age": 18, "height": 1.71, "is_male": True, "hobit": ["抽烟","喝酒","烫头"]}
print(my_dict2)#{内容}
print(len(my_dict2)) #5


#字典的操作

#增加和修改 语法是一样的

"""
语法:
字典[key] = value数据值
1.如果key已经存在,就是修改数据
2.如果key不存在,就是添加数据(即添加键值对)
"""

#定义字典 小米,18,爱好
my_dict = {"name":"小明", "age":18, "hobby":["抽烟","喝酒","烫头"]}
print(my_dict)

#1.添加性别信息 sex
my_dict['sex'] = '男'
print(my_dict)

#2.修改年龄为19
my_dict['age'] = 19

#3.添加一个爱好,学习,本质是向列表中添加一个数据 my_dict[key]就可以理解为把数据取出
my_dict["hobby"].append("学习")
print(my_dict)  #{'name': '小明', 'age': 19, 'hobby': ['抽烟', '喝酒', '烫头', '学习'], 'sex': '男'}

#字典的删除
"""
删除指定键值对
del my_dict[key]

清空
my_dict.clear()
"""

#删除 sex键值对
del my_dict["sex"]
print(my_dict)

#清空键值对
my_dict.clear()
print(my_dict) #{}

#字典.pop("key")
my_dict = {"name":"小明", "age":18, "hobby":["抽烟","喝酒","烫头"]}

pop_out = my_dict.pop("name")# Python 字典本身的 pop() 方法不能直接返回键值对,它只返回"值".

print(f"pop name后的字典是: {my_dict}")
print(f"pop key变量接受的是返回的value")
print(f"pop_out存储的值value是:{pop_out},类型是:{type(pop_out)}")#pop_out存储的值value是:小明,类型是:<class 'str'>

#dict.popitem() 方法  
#所以你要是想从 dict 中一次性拿出"键+值",就用 .popitem(),返回值是 (key, value) 的元组,能被变量接住操作.
d = {'x': 10, 'y': 20}
item = d.popitem()
print(item)  # ('y', 20) _ 注意是最后一个插入的键值对
print(type(item))  # <class 'tuple'>

# 删除抽烟的爱好,本质是在列表中删除数据
my_dict['hobby'].pop(0)
print(my_dict)

my_dict = {"name":"小明", "age":18, "hobby":["抽烟","喝酒","烫头"]}
my_dict['hobby'].remove('抽烟')
print(my_dict)


"""
容器类型	方法	      返回内容	                 返回类型
list	  .pop()	    最后一个元素	            元素类型本身
set	      .pop()	    随机一个元素	            元素类型本身
dict	  .pop(k)	    指定 key 的 value	       元素类型本身
dict	  .popitem()	最后一个 (key, value)	   tuple
"""



# 查询 inquiry - 根据key获取对应的value
# 字典中没有下标的概念,想要获取数据值要使用key来获取

#1. 使用 dic[key]
    #1.如果key存在,会返回key对应的value
    #2.如果key不存在,会报错
    
#使用 dict.get(key) dict.get(key,value)
    #1. 数据值一般不写,默认是None
    #返回
    #1.如果key存在,返回value
    #2.如果key不存在,返回的是   (None)
    
# 一般建议使用 get 方法 
    
my_dict = {"name":"小明", "age":18, "hobby":["抽烟","喝酒","烫头"]}
# 1.获取名字
print(my_dict['name'])
print(my_dict.get('name'))

# 2.获取不存在的key,获取'gender'
# print(my_dict['gender']) 会报错,keyError
print(my_dict.get('gender'))       # None
print(my_dict.get('gender','male'))       # male
"""
实际是dict.get('key', default)
"如果字典里有 'gender' 这个键,就返回它对应的值;
如果没有,就返回 'male',但不修改原字典."
"""
print(my_dict) # {'name': '小明', 'age': 18, 'hobby': ['抽烟', '喝酒', '烫头']}

my_dict.setdefault('gender', 'male')
# 会返回 'male',并且把 'gender': 'male' 加进字典
print(my_dict)
#{'name': '小明', 'age': 18, 'hobby': ['抽烟', '喝酒', '烫头'], 'gender': 'male'}

# 3.获取第2个爱好 先找到list,再对list进行处理
print(my_dict['hobby'][1])
print(my_dict.get('hobby')[1])


# 4.字典的遍历,从容器当中把元素一个一个取出
"""
3种遍历
1.key iterate
2.value
3.key: value

key进行遍历:
for variable in dict:
    print(variable) # key
    
for variable in dict.keys(): dict.keys() 可以获得字典中所有的key
    print(variable)
    
    
    
value进行遍历:
for variable in dict.values():
    print(variable)
    
key:value interate

for variable1, variable2 in dict.items():  dict.items()获取键值对
    print(variable1,variable2)


"""

# 定义字典
my_dict = {'name':"小明",'age': 18, 'gender': 'male'}

# iterate key
for k in my_dict:
    print(k)
    
for k in my_dict.keys():
    print(k)
    
print("-" * 30)


# iterate value
for v in my_dict.values():
    print(v)

# 3iterate key:value
for k,v in my_dict.items():
    print(k,v)  
    
   





