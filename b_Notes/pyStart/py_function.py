name = "hello world"
length = len(name)
print(length)


# 函数示例
def my_len(data):
    count = 0
    for i in data:
        count += 1

    return count


def addPrint(x, y):
    result = x + y
    print(f"{x} + {y} is %d" % result)


def add(x, y):
    sum = x + y
    return sum


# 函数调用
print("add函数被调用了,返回值是: %d" % add(1, 1))


# 函数传参
def user_info(name, age, gender):
    print(f"you name is {name}, age is {age}, gender is {gender}")


user_info(name="nn", age=18, gender="male")  # 位置参数
user_info(age=19, name="nn", gender="famale")  # 可以不按照顺序固定
user_info("nn", age=20, gender="bio")  # 如果混合使用,那么位置参数必须在最前面


# 函数多返回值
def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)



def add2(a: int, b: int) -> int:
    return a + b

# print(add(3, "5"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'



"""
定义函数:
def 函数名(参数):
    函数体
    return 返回值
    
调用函数: 变量名 = 函数名(参数)
或者对于"返回值是None"比如里面是print语句的函数直接调用就行了 

<class 'NoneType'>

"""

def say_hi():
    print("Hello world")
    
result = say_hi()

print(f"{type(result)}")


def say_hi2():
    print("Hello")
    return None

result2 = say_hi2()

print(f"{type(result2)}") #<class 'function'>


# -----------函数的作用域-------------- global 全局变量

num = 200
def test_a():
    print(f"test_a: {num}")
    
def test_b():
    # global num
    num = 500
    print(f"test_b: {num}")
    
test_a()    #200
test_b()    #500
print(num)  #200
