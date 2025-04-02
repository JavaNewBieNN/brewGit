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

