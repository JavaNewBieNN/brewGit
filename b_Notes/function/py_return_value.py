#-------函数的多返回值--------
"""
其实 Python 的函数并不是真的返回多个值,而是:

	✅ 返回了一个"元组"(tuple),然后你可以用多个变量来接收它.
 
"""


def test_return():
    return 1, 2

x, y = test_return()
print(x)
print(y)

# ------------------------------------------
def get_user():
    return "张三", 18, "男"  # 本质上是 return ("张三", 18, "男")

name, age, gender = get_user()  # 解包(tuple unpacking)



#------------------------------
"""
❓为什么 Python 要设计"多返回值"?

✅ 1. 让函数能一次返回多个相关信息,逻辑更清晰

比如你写一个除法函数,既要返回"商"又要返回"余数":
"""
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(10, 3)

"""
传统语言你要么:
	•	返回结构体(C)
	•	返回对象或数组(Java)
	•	传入 pointer 或 reference 修改原变量(C/C++)

用 Python 就一行搞定,极其优雅.
"""

"""
print() ---> None
input() ---> 键盘输入的内容
"""




