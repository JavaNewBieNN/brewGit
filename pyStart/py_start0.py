print("Hello world")
# 单行注释
'''
多行注释
变量不能是数字开头
大写表示常量

数据类型：
数字

'''
a = 10  # 整数
b = 20
# 字符串
s = "周润发"
s2 = '周润发'
print(s)
print(s2)
a1 = """
Hello world1
Hello world2
Hello world3
"""
print(a)
print(a1)

print("nn\n" * 5)
signal = False
print("print something" + " print something2")
# print("something" + 1) 报错 type error
# print("print something" + a) 还是type error，发现不能不一样的相加
print("print something" + a1)

print("-------------------")
a = 10
print(type(a))
a = "nihao"
print(type(a))
typeOfa = type(a)  # <class 'str'>

# python 中做print语句做多份输出 print(content1, content2, content3 ...);


# -------------------数据转换--------------------
# 数字转换成字符串num

print("====================")
val = 11
numToStr = str(val) # 开辟了新的内存地址，numToStr指向了新的内存，str（）这种转型函数的本质是开辟了新的内存，而不是真的把原有的数据的类型给转换了
print(type(val)) # <class 'int'> ，所以我们有了第三行代码，发现val仍然是指向int，val不会被解释器回收
print(type(numToStr), numToStr)  # <class 'str'> 11

# 字符串转数字
# num3 = int("Hello world'")会报错，只有 纯数字字符串能转
num3 = int("123")
print(num3)

# 浮点数转整数
int_num = int(11.7345)
print(type(int_num), int_num) # 11 不是四舍五入，小数部分会被舍弃

# 整数转浮点数
float_num = float(11)
print(type(float_num),float_num) # <class 'float'> 11.0




"""

说说我的理解你看看对不对。从c的角度来理解，这个a相当于是一个指针变量，每次赋值的时候开辟一个内存，
然后把c指向这里，然后原有的内存没有引用（指针指着了）了，然后python的解释器里面有类似于jvm的东西，
会自动回收垃圾数据，java里面一段时间没有引用的内存会被看作垃圾数据被jvm回收。我理解的对吗?

ChatGPT 说：

你的理解非常接近，解释得很不错！我们可以从以下几个方面来确认你的理解：

指针的概念： 在C语言中，变量a如果是一个指针，每次赋值都会使指针指向新的内存地址。你将Python中的变量a类比为C中的指针，这是非常准确的。在Python中，变量实际上就是一个引用，类似于指针，指向内存中的对象。每次你赋值的时候，Python会在内存中分配空间并让a指向新对象。

内存管理： 就像你说的，原有的内存如果没有其他引用指向它，它就变成了“垃圾数据”。Python有一个类似于Java中JVM的垃圾回收机制（Garbage Collection, GC）。当内存中的对象没有任何引用（即没有变量指向它），垃圾回收器会标记它为可回收，并在适当的时候释放这些内存。

自动垃圾回收： 和Java一样，Python的垃圾回收器也会自动回收不再被引用的内存，防止内存泄漏。在Java中，这是通过JVM完成的，而在Python中，解释器有一个类似的机制。你提到Java会在一段时间后回收没有引用的内存，这同样适用于Python。

总结来说，你从C语言的角度理解Python的变量和内存管理是非常正确的。Python中的变量可以看作是指向对象的引用（类似指针），垃圾回收器会负责回收不再被引用的内存。你对这两个语言的类比和内存管理机制的理解非常到位！

"""
