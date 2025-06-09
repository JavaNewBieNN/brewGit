class Student:
    
    name = None
    age = None
    tel = None
    
    # 构造方法的名称不变就这么写
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")
        
        
    def __lt__(self, other): #一般比较小于
        return self.age < other.age
    
    
    def __le__(self, other):
        return self.age <= other.age        
    
    def __eq__(self, other):
        return self.age == other.age
        
        
    def __str__(self):
        return f"Student类对象, name:{self.name}, age:{self.age}"

    def __del__(self):
        print(f'{self.name}没了，给它处理后事')
    
    
"""
什么是魔法方法？
魔法方法就是名字前后都有两个下划线（__）的特殊方法
这些方法不是你主动调用的，而是 Python 在特定情况下自动调用的。就是不写也有，写了就是override 跟java的 toString那种一样

"""


stu1 = Student("jayzhou",31,"12345678")
stu2 = Student("ljj",31,"33114")

print(stu1.name)
print(stu1.age)
print(stu1.tel)

print(str(stu1))

# 类的比较

students = [Student("Alice",13,"1234"),
            Student("Bob",11,"1234"),
            Student("Charlie",12,"12345")]

# 直接用 sorted() 排序,自动调用 __lt__
sorted_students = sorted(students)

for student in sorted_students:
    print(f"{student.name}: {student.age}")
    

print(stu1 == stu2) #默认比较内存地址 
print(stu1 < stu2)

"""
class class_name:

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        
    def func_name(self): 第一个参数要是self
        pass
        
        
        
        
"this 居然是 implicit 的，原来是传对象地址进去，属性值就存在地址里。"

这正是关键。

在 Java 中你以前写：

java
复制
编辑
Cat cat = new Cat();
cat.meow();
你没意识到的是，其实 JVM 背后等价于：

java
复制
编辑
Cat.meow(cat);  // 隐式传入 this
然后 meow() 方法内部访问 this.name，其实是：

java
复制
编辑
cat.name  // 只是写成了 this.name 看起来更优雅而已
"""