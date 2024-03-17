class Person:
    def __init__(self, name, age):
        self.name = name  # 公有变量
        self.age = age    # 公有变量
        
person = Person("Alice", 25)
print(person.name)  # 输出: Alice
person.age = 26
print(person.age)   # 输出: 26