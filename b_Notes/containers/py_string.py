"""
字符串是字符的容器
一个字符串可以存放任何数量的字符
字符串是一个不可修改的容器
增删改是不可完成的,如果必须要做只能是一个新的字符串
"""

my_str = "itheima and itcast"

# 通过下标索引取值
value = my_str[2]
print(f"2号元素是: {value}") # h


# index 方法
value = my_str.index("and")  # 8 
print(f"在字符串{my_str}中查找and,其起始下标是:{value}")

# replace 方法  
new_my_str = my_str.replace("it", "黑马")
print(f"replace过后的字符串是: {new_my_str}")

# split 方法
my_str= "hello python itheima itcast"
my_str_list = my_str.split(" ")  #['hello', 'python', 'itheima', 'itcast'],类型是<class 'list'>
print(f"将字符串{my_str}进行split切分后得到:{my_str_list},类型是{type(my_str_list)}")


# strip    它的作用是 "去掉字符串前后不需要的部分(如空格或特定字符)"
text = "  hello world  "
print(text.strip())  # "hello world"

text = "xxxhello worldxxx"
print(text.strip("x"))  # "hello world"

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")  #其实是去除字符串1,和字符串2,两个都去除
print(f"字符串{my_str}被strip('12')后,结果是:{new_my_str}")


# 统计字符串中某字符串出现的次数
my_str = "12itheima and itcast21"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是:{count}")

# 统计字符串的长度
num = len(my_str)



"""
语言	           字符串是否不可变(immutable)                      字符串是对象吗?             类型说明
Python	          ✅ 是不可变的                                   ✅ 是对象                  str 是 Python 内置类,一切皆对象
Java	          ✅ 是不可变的                                   ✅ 是对象                  String 是一个类(java.lang.String)
C	              ❌ 否,C 中字符串是可变的(但也可以模拟不可变)



🧠二、什么是"字符串不可变"?
"不可变" (immutable) 是说:字符串一旦创建,其内容就不能被更改.
比如:

s = "hello"
s[0] = "H"   # ❌ 报错,不能直接修改字符串中的某个字符
你不能直接修改字符串中的字符,只能通过"创建一个新的字符串"来实现修改:

s = "hello"
s = "H" + s[1:]   # ✅ 创建了一个新字符串 "Hello"

s = "hello"
s = s.replace("h", "H")

java和python很像:

Python 的过程简述:
"hello" 是一个 str 对象,存在堆内存中.

s 是变量名,指向 "hello".

调用 replace() 会创建一个新的字符串对象 "Hello".

s 被更新为指向 "Hello".

"hello" 原对象依然存在,只是 s 不再引用它(可能被垃圾回收)



📌 总结一句话:
在 Java 或 Python 中,对字符串做修改操作(如 replace())并不会改变原对象,
而是生成一个新的字符串对象并返回,变量 s 再指向新的对象,旧的字符串对象保持不变.



对于c语言:
char s[] = "hello";
s[0] = 'H'; // ✅ 合法,变成 "Hello"

"""