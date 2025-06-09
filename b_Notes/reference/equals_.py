"""
✅ Java 中的对象比较

==：比较的是内存地址（引用是否相同）。
.equals()：默认也是比较地址，除非你 override equals() 方法

String a = new String("hello");
String b = new String("hello");

System.out.println(a == b);        // false -> 比较地址
System.out.println(a.equals(b));   // true  -> 比较内容（因为 String 类重写了 equals）

✅ Python 中的对象比较
1. == 比较的是内容（调用 __eq__ 方法）
如果没有重写 __eq__，就退回到默认的行为（比较地址）

所以，你可以通过重写 __eq__ 来自定义“什么叫相等”
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Alice")

print(p1 == p2)  # False，默认是比较地址
现在重写 eq方法
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

p1 = Person("Alice")
p2 = Person("Alice")

print(p1 == p2)  # True，因为我们定义了“名字相同的人算一样”

✅ Python 中 is 才是比较地址
p1 is p2  # False -> 比较的是 id(p1) == id(p2)

| 比较方式        | Java                     | Python                    |
| -----------   | -----------------        | ------------------------- |
| `==`          | 比较地址                  | 比较值（调用 `__eq__`）          |
| `.equals()`   | 比较值（需手动 override）  | 无，统一用 `==`，但 `__eq__` 可重写 |
| 比较地址       | `==`                     | `is`                      |


"""