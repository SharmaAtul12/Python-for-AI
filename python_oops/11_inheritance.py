# Inheritance :-> Inheritance is a mechanism in object-oriented programming that allows a class (called the child or subclass) to inherit properties and behaviors (methods) from another class (called the parent or superclass). 
# This promotes code reusability and establishes a relationship between classes.

# Types of Inheritance :->

# 1. Single Inheritance :-> A child class inherits from a single parent class.

# This is the example of single inheritance where ToyotaCar class is inheriting from Car class.
class Car:
    @staticmethod
    def start():
        print("Car Started ...")

    @staticmethod
    def stop():
        print("Car Stopped ...")

class ToyotaCar(Car): # Yha pp hamne Inheritance ka use kiya h , ToyotaCar class ne Car class ko inherit kiya h , to ToyotaCar class ke paas Car class ke sare methods aa gaye h ..
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Toyota")
car2 = ToyotaCar("Fortuner")

# So yha pp Car ke methods ko ToyotaCar class ke object ke through access kr skte h .. 
car1.start() # Car Started ...
car2.stop()  # Car Stopped ...





# 2. Multi-level Inheritance :-> A child class inherits from a parent class, and then another class inherits from that child class.
class Car:
    @staticmethod
    def start():
        print("Car Started ...")

    @staticmethod
    def stop():
        print("Car Stopped ...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start() # Car Started ...
car1.stop()  # Car Stopped ...
# This will raise an error because brand is not defined in Fortuner class . 
print(car1.brand) 
print(car1.type) # Diesel



# 3. Multiple Inheritance :-> A child class inherits from multiple parent classes.

class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to Class B"

class C(A, B): # Yha pp C class ne A and B class ko inherit kiya h , to C class ke paas A and B class ke sare methods aa gaye h ..
    varC = "Welcome to Class C"

c1 = C()
print(c1.varA) # Welcome to Class A
print(c1.varB) # Welcome to Class B'
print(c1.varC) # Welcome to Class C