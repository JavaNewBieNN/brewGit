"""
list去重:list中存在多个数据,需求,去除列表中重复的数据
"""

#方式1:遍历原列表中的数据,判断在新列表中是否存在,如果存在,不管,如果不存在,则放入新列表中
"""
遍历,判断是否存在:可以使用 in
存入数据:append()
"""
my_list= [4,3,1,2,3,1,4,1,2,3,3,2,1,2,3,1]
new_list = list()

for i in my_list:
    if i in new_list:  # if i not in new_list: new_list.append()
        continue
    else:
        new_list.append(i)


print(new_list)            


#方法2 利用set(),集合中不能有repeat的数据,如果有重复的数据会自动去重,利用集合的特点对列表去重
"""
1.使用 set()类型转换将列表转换为 集合类型
2.再使用list()类型将集合转换为列表

缺点:不能保证数据在原列表中出现的顺序(一般来说也不考虑这件事),可能是升序
"""

my_list= [1,2,3,3,2,1,2,3,1]
my_set = set(my_list)
print(my_set)

relist = list(my_set)
print(relist)
print(list(set(my_list)))





