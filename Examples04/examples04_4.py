#类的继承和多态示例

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self, words):
        print(f"{self.name} says: {words}")
        
    def walk(self, distance):
        print(f"{self.name} walks {distance} meters.")
        
    def eat(self, food):
        print(f"{self.name} eats {food}.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def study(self, subject):
        print(f"{self.name} studies {subject}.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def teach(self, topic):
        print(f"{self.name} teaches {topic} in {self.subject}.")


student = Student("Alice", 20, "S001")
teacher = Teacher("Bob", 35, "Math")

people = [student, teacher]

for person in people:
    person.speak("Hello!")
    person.walk(10)
    person.eat("lunch")
    
    if isinstance(person, Student):
        person.study("Python")
    elif isinstance(person, Teacher):
        person.teach("Algebra")