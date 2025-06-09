"""
在python中定义的方法和属性，可以添加访问控制权限

public：
    直接书写的方法和属性，都是public的，可以在任何地方访问和使用

private
    在类的内部 __attribute_name 这样定义
    私有的方法和属性，只能在当前类的内部使用


    什么时候定义私有？
        某个属性或者方法不想在类外部被访问和使用，就将其定义为私有
        在测试中一般不怎么使用，直接公有即可
        开发中会根据文件确定什么为私有

python中私有的本质，在python解释器执行代码，发现属性名或者方法名字前面有两个__，会将这个名字重命名
会在这个名字的前边加上_className, 即 self._age =====> self._Person__age

6.如果一定要在class的外部操作私有属性，方法是在类的内部定义公有的方法，我们通过这个方法去操作

"""
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.__age}'


xm = Person('xm', 18)
print(xm)

xm._Person__age = 20   # 能用，但是不建议用
print(xm)  #20
# print(xm.__age)在类的外部不能修改私有属性


#补充，object._dict_ 魔法属性，可以将对象具有的属性组成字典返回
my_dict = xm.__dict__ #{'name': 'xm', '_Person__age': 20}
print(my_dict)