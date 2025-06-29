"""
python中 函数的 参数传递 以及 返回值 都是靠 引用 传递的



"""

"""
变量的引用
1.在定义变量的时候 变量 = 数据值, python解释器会在内存中开辟两块空间
2.变量和数据都有自己的空间
3.日常简单理解,将数据保存到变量的内存中,
    本质是将 数据的地址 保存到变量对应的内存中
    


✅ 1.1 变量和指针在 C 中确实都存储在栈(stack)中

假设你写:
int a = 10;
int *p = &a;

	•	a 是变量,值为 10,存在 stack 的某个地址,假设是 0x666
	•	p 是一个 指针变量,它本身也存在 stack 中,存的是 a 的地址:0x666
 
栈内存:
地址         内容
0x1000      0x666        ← p(指针变量,值是地址)
0x666       10           ← a(实际数据)




✅ 1.2 那你说得对:为什么不让变量本身就"是指针"?

比如我写 int a = 10;,为什么不让 a 本身就是一个"地址变量"?
	•	理论上这是可行的,但为了易读性和类型安全性,C 语言才把变量和指针分开
	•	a 是值,*p 是通过地址间接获取的值
	•	如果你用 a,C 就直接知道你要操作的是值;你用 *p,C 才知道你要"沿着地址访问内存"

🔧 C 是"显式内存控制语言",它希望你对"值"和"地址"的操作是显式分开的


✅ 1.3 C 变量名的意义是什么?变量名到底"存在哪"?

变量名本身并不"占内存"_它是编译器在编译时用来建立符号表的标识符
	•	编译器会给 a 分配一段内存,比如 0x666
	•	在你写 a = 10; 的时候,实际上是对 0x666 这个内存地址赋值
	•	所以你写 a,其实就是编译器在帮你隐式操作 &a

✅ 你说得完全对:C 语言里,变量名其实就是一个"简洁可读的地址别名"
记住

🌟 Part 2:Python 中变量 = 引用 = 类似于 C 中的指针?
    
"""