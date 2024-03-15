#函数返回值

def get_name():
    return "Eric"
    
def get_name_and_age(): 
    return "Eric", 30

name = get_name()
print(name)

name, age = get_name_and_age()
print(name, age)