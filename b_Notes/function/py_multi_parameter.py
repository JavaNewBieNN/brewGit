"""
传递的参数和定义的参数的顺序以及个数必须一致
"""

def user_info(name,age,gender):
    print(f"您的名字是:{name},your age is {age},your gender is {gender}")
    

#关键字穿惨,可以不按照顺序,顺序无所谓,
user_info( age=20, gender= "male",name = 'ning')

#也可以两种方式混用,但是位置参数必须在最前面
user_info("ning",age = 20, gender= "male")



"""
def定义的是带有名称的函数
lambda关键字可以定义匿名函数,只能临时使用一次
"""

def test_func(compute):
    result = compute(1,2)
    print(result)
    
def compute(x,y):
    return x + y

test_func(compute)

#----------lambda---------  写法  fuc(lambda 参数1, 参数2, 参数3, ... : 逻辑)  只能写一行
test_func(lambda x, y: x + y)