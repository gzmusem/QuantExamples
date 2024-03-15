#函数定义和调用,可变参数

def sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total  
print(sum())
print(sum(1, 2, 3))