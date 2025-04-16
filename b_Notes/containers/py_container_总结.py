"""
1.序列支持加法运算,序列就是有index的
string,list,tuple 支持加法运算

str1 = 'hello' + ' world' # 'hello world'

list1 = [1,2] + [3,4]   # [1,2,3,4]

tuple = (1,2) + (3,4)   # (1,2,3,4)

2.序列 list string tuple 支持 乘以 一个数字

'hello ' * 3      # ===> 'hello hello hello '
[1,2] * 3 # =====> [1,2,,1,2,1,2]
(1,2) * 3 # =====> (1,2,1,2,1,2)

3. len() 在容器中都可以使用

#. in 关键字在容器中都可以使用,注意,在字典中判断的是字典的key是否存在
nums = [1, 2, 3]
print(2 in nums)     # True
print(5 in nums)     # False    


person = {'name': '小明', 'age': 18}
print('name' in person)   # True ✅ 判断 key 是否存在
print('小明' in person)   # False ❌ value 不参与判断



"""