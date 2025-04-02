"""
if condition:
    print()   四个空格做缩进一个tab
    
print("something else")
"""


height = int(input("请输入你的身高: "))
vip_level = int(input("input your vip level"))


if height < 120:
    print("free")
elif vip_level > 3:
    print("free")

else:
    print()
    
print("have fun")

