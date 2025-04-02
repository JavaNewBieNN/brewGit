
"""
序列: 内容连续,有序,可以使用index的数据容器
序列容器: str,tuple, list
切片: 从一个序列中,取出一个子序列
list[start_index:end_index:step] 从start开始包括start,留空表示从index = 0开始. 到end结束, 不包括end
步长尾1表示一个个取元素
步长为N, 每次跳过N-1个元素取
步长为负数表示,反向取(起始下标和结束下标也要反向标记) 就是从正的index取,想想要取哪一段?从这个地方的index取,然后到要断掉的地方的index - 1,然后步长为-几就可以了
"""
my_list = [0,1,2,3,4,5,6]

#从index = 1 开始,到index = 4 结束
result = my_list[1:4:1]
print(f"结果1:{result}") #[1,2,3]

#步长默认为1,所以可以省略不下
resul1 = my_list[1:4] 
print(f"结果1:{resul1}") # [1,2,3]

#对tuple进行切片,从头开始,最后结束,步长1
my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[:]
print(f"结果2:{result2}")

#对str进行切片从头开始,到最后结束,步长为2
my_str = "01234567"
result3 = my_str[::2]
print(f"result3是:{result3}")

#对str进行切片,从头开始,到最后结束,步长-1
my_str = "01234567"
result4 = my_str[::-1]
print(f"result4是:{result4}")

#对列表进行切片,从3开始,到1结束,步长-1
my_list = [0,1,2,3,4,5,6,7]
result5 = my_list[3:1:-1]
print(f"result5是:{result5}") #【3,2】

#对元组进行切片,从头开始,到尾结束,步长为-2
my_tuple = (0,1,20,3,34,3,123,1244,1,0)
result6 = my_tuple[::-2] 
print(f"result6试{result6}") #[0,1244,3,,3,1]



"""
practice: string: "学python,来黑马程序员,月薪过万"
请使用任何方式得到"黑马程序员"
"""
#---------------思路1--------------
str1 = "学python,来黑马程序员,月薪过万"

reverse = str1[::-1]
print(f"{reverse}")

reverse2 = str1

split = reverse2[9:14:1]

print(f"{split}")

