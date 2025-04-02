
for i in range(5):  # 相当于 for (int i = 0; i < 5; i++)
    print(i)


# 也可以指定开始和步长
for i in range(10, 0, -1):  # 从10递减到1 
    print(i)


"""
Java 写法	                            Python 等价写法	                   说明
for (int i = 0; i < 5; i++)	           for i in range(5):	             从 0 到 4,共 5 个
for (int i = 2; i < 10; i++)	       for i in range(2, 10):	         从 2 到 9
for (int i = 10; i >= 1; i--)	       for i in range(10, 0, -1):	     从 10 到 1,步长 -1
for (int i = 0; i < 10; i += 2)	       for i in range(0, 10, 2):	     从 0 到 8,间隔 2
"""