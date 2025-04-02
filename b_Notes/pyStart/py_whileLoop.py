import random
num = random.randint(1,100)


# ------- while loop -----------
"""
while condition:
    do something
"""

#求1-100的和

sum = 0
count = 1
while count < 101:
    
    sum = sum + count
    count = count + 1
    
print(sum)


"""
while 猜数字

无限次机会知道猜中
每一次猜不中提示大了或者小了
猜完数字后提示猜了几次

"""

print("猜数字游戏")
guess = int(input("input your guess: "))

while guess != num:
    
    if guess > num:
        print("too large, once again. ")
    elif guess < num:
        print("too small, once again. ")
    else:
        break
    
    guess = int(input("input your guess: "))
    
print("bingo!")

print("-------------------------------------------------")


"""
通过while循环,输出99乘法表
"""


row = 1
while row < 10:
    column  = 1
    
    while column <= row:
        result = row * column
        print(f"{column}*{row}={result} \t", end = "")
        column = column + 1
        
    
    print()
    
    row = row + 1
    


