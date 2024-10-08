name = ''
name1 = ""
name2 = """ """

# 这里会自己换行
name4 = """

hello 
world

"""
print(name4, type(name4))
someString = "\""  # "
print("\"\"")  # \ 这个玩意后面的引号就变成字符串了
print(someString)

# +号能够拼接 字面量+字面量， 还有 字面量+变量 只能完成字符串本身的拼接
someString1 = "123"
num = 123
someString2 = "456"

print("123" + someString2)

# print("123" + num) type error
# print(someString1 + num + someString2) 会产生type error
print("-----------------------------------------------")
"""
字符串格式化：
思考，+号不能拼接不同的类型
"""
age = 100
dkLength = 20.9
message = "I am %d years old and my dk length is %f cm" % (age, dkLength)  # 多个变量要用括号括起来，并且按照顺序填入
print(message)

print("I am %d years old and my dk length is %f cm" % (age, dkLength))  # 20.900000

# 格式化的精度控制
"""
可以使用辅助符号m.n来控制数据的宽度和精度 mn都要是数字
m 控制要被打印的数字的宽度
n 控制小数精度
"""
print("I am %d years old and my dk length is %3.1f cm" % (age, dkLength))  # 20.9
print("I am %d years old and my dk length is %.1f cm" % (age, dkLength))  # 20.9
