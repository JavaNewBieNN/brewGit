# -------- for loop ------------
# for 循环的语法格式 for 临时变量 in 序列
name = "ning nie"
for x in name:
    print(x)

i = 0
while i < 10:
    i = i + 1
    print("第%d组" % i,end="")
    j = 0
    while j < 10:
        j = j + 1
        print(j, end="")
    print()
print("done")
