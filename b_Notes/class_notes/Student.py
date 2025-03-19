class Student:
    """
    在Python中,你不需要像在Java中那样先在类的最前面定义成员变量
    (fields),然后再在构造器(__init__ 方法)中初始化。在Python中,成员变量通常直接在构造器中初始化。
    这是因为Python的类不需要预先声明属性,属性是在使用的时候动态创建的。
    
    只有通过self类才能够类的成员变量

    成员方法的语法
    def 成员方法(self, 参数列表):
        方法体
        return
    """

    name = "nn"
    genderr = None # 可以声明也可以不声明
    
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        
        
    
    
    
