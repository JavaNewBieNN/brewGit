"""
文件操作步骤：

1.打开文件
(function)
def open(
    file: FileDescriptorOrPath,    就是要打开的文件，类型是字符串，path可以是相对的或者绝对的，建议相对（当前文件在的路径）  比如 data/hello.txt
    mode: OpenTextMode = "r", 默认default是 只read，{只write，清空原内容，} append，文件末尾写入内容， r+读写
    encoding: str | None = None,类型：字符串，如 "utf-8"、"gbk"，默认是系统默认编码，作用：打开文本文件时指定字符编码（读写中文时特别重要）

                            尽量手动指定 "utf-8" 以避免乱码问题
) 
返回值：返回的是文件对象，对后续文件的操作都需要这个对象

2. 写这些文件，前提文件的打开方式是w或者是a
file.write("写入文件的内容")
#写入文件的字符数，一般不关注

   读文件就是打开方式要是r
   file.read(n) file是文件对象，n表示读取多少个字符，一般不写，表示读取全部内容，返回值是读取到的文件内容，类型是字符串

3.关闭文件： 将文件占用的资源进行清理，同时会保存文件，文件关闭之后这个文件对象就不能使用了
文件对象.close()

"""
#1,打开文件
f = open('a.txt','w',encoding='utf-8') # w 打开会直接清空原文件，然后再写

#2,写文件
f.write("好好学习\n")
f.write("天天向上\n")

#3,关闭文件
f.close()


f = open('a.txt','a',encoding='utf-8')
f.write("nihao")
f.close()

# ----------------------------------- 读文件
# 1.打开文件
f = open('a.txt','r',encoding='utf-8')

# 2.读取文件
"""
file.read() 不会自动分行，它只是把所有内容作为一个整体字符串返回。

如果你想按行处理，可以用：

file.readlines() → 返回每一行组成的列表
"""
buf = f.read()   # 返回的是一个字符串
print(buf)  # buf 就是拿到了文件的内容

#3.关闭文件
f.close()


#--------------------------------------------------------------
"""
题目：Hello world! This is a unit_tests. This unit_tests is simple. Hello again!
Most frequent word: this
Count: 2
说明：忽略大小写和标点，this 和 This 视为同一个词
"""

f = open('sample.txt','r',encoding='utf-8')

txt = f.read()

txt = txt.lower()


# ---------------------------------------------
"""
使用with open() 打开文件的好处：不用自己去书写关闭文件的代码，会自动进行关闭

"""

with open('a.txt','a',encoding='utf-8') as f:
    f.write('good good study')
# append 方式打开文件，如果文件不存在那么创建文件，如果文件存在，则在末尾写入内容

# -------------------按行读取内容

