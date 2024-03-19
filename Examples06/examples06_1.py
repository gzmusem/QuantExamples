#异常处理

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("除数不能为零!")
    else:
        print(f"{a} 除以 {b} 的结果是: {result}")
    finally:
        print("除法运算完成。")

# 测试函数
divide(10, 2)
divide(10, 0)