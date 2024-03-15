#函数定义和调用 关键字参数

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
        
print_info(name="David", age=30, city="New York")