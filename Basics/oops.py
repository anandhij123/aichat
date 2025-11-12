#self refers to the specific instance of the object that is being operated on.  
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof! Woof!")

class Owner:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone_number = phone

    def speak(self):
        print("My name is", self.name)

owner1 = Owner("John", "123 Main St", "555-1234")   

dog1 = Dog("bruce", "bulldog", owner1)
print(dog1.name)
print(dog1.breed)
'''print(dog1.owner.name)  '''
dog1.bark()
print(dog1.owner.phone_number)
dog1.owner.speak()  

owner2 = Owner("Sally", "123 Main St", "555-1234")
dog2 = Dog("freya", "Scottish Terrier", owner2)
print(dog2.owner.name)
print(dog2.name)
print(dog2.breed)
dog1.bark()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

    def talk(self):
        print("Hello, my name is", self.name)

    def walk(self):
        print(self.name, "is walking")

    def get_older(self):
        self.age += 1
person1 = Person("John", 36)
person1.greet()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def sendgreeting(self, user):
        print(f"Hello {user.name}, welcome to our site!.My name is {self.name} and my email is {self.email}")

user1 = User("John", "john@gmail.com")
user2 = User("Sally", "sally@gmail.com")
user1.sendgreeting(user2)
#Traditional approach to make the data private and use getters and setters
#Private data is not accessible outside the class.eg. __name
#protected data is accessible only within the class and its subclasses.eg. _name. Internal use only.For better readability
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age

student1 = Student("John", 36)
print(student1.get_name())
print(student1.get_age())
student1.set_name("Sally")
student1.set_age(25)
print(student1.get_name())
print(student1.get_age())
