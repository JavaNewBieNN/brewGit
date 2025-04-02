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

# +号能够拼接 字面量+字面量, 还有 字面量+变量 只能完成字符串本身的拼接
someString1 = "123"
num = 123
someString2 = "456"

print("123" + someString2)

# print("123" + num) type error
# print(someString1 + num + someString2) 会产生type error
print("-----------------------------------------------")
"""
字符串格式化:
思考,+号不能拼接不同的类型
"""
age = 100
dkLength = 20.9
message = "I am %d years old and my dk length is %f cm" % (age, dkLength)  # 多个变量要用括号括起来,并且按照顺序填入
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


'''
在 Python 中,最常见的标准输出语句是 print(),而连接不同类型的值通常有以下几种方式:
'''
#1 逗号 , 连接(自动加空格,不需要转换类型):
print("Hello", "world", 123, True) # Hello world 123 True

#2 字符串拼接 +(仅适用于字符串,需要手动转换类型):
print("Hello " + "world " + str(123) + " " + str(True)) # Hello world 123 True

#3 f-string(推荐,最简洁直观):
print(f"Hello world {123} {True}") # Hello world 123 True

#4 使用占位符
print("I am %d years old and my dk length is %.1f cm" % (age, dkLength))  # 20.9

# f"..."(f-string)能够自动将所有类型的数据转换为字符串,并进行拼接,无需手动 str() 转换.
num = 123
boolean = True
lst = [1, 2, 3]
dic = {"key": "value"}

print(f"somestring1 somestring2 {num} {boolean} {lst} {dic}")
# somestring1 somestring2 123 True [1, 2, 3] {'key': 'value'}

#定义所需变量
name = "suning"
stock_price = 19.99
stock_code = "003032"

# 股票 价格 每日 增长 因子
stock_price_daily_growth_factor = 1.2
growth_days = 7

"""
经过增长天数后股价达到了多少钱?
用字符串进行格式化输出,如果是浮点数,要求小数点精度2位
"""

current_price = stock_price * stock_price_daily_growth_factor ** growth_days

print("----------------------------------------------------")

print(f"公司: {name}, 股票代码: {stock_code}, 当前股价: {current_price}")
print("每日增长系数为: %f 经过%d天的增长后,股价达到了:%.2f" % (stock_price_daily_growth_factor, growth_days, current_price))




#-------------字表符--------------
print("Hello\tworld")
print("itheima\tbest")

 