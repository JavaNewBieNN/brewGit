name = "hello world"
length = len(name)
print(length)


# 函数示例
def my_len(data):
    count = 0
    for i in data:
        count += 1

    return count


def add(x, y):
    result = x + y
    print(f"{x} + {y} is %d" % result)
