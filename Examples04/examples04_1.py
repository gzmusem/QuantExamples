class Person:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        
    def speak(self, words):
        print(f"{self.name} says: {words}")
        
    def walk(self, distance):
        print(f"{self.name} walks {distance} meters.")
        
    def eat(self, food):
        print(f"{self.name} eats {food}.")


person = Person("Alice", 25, "Female", 165)

person.speak("Hello, how are you?")
person.walk(500)
person.eat("an apple")