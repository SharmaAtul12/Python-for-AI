# Class method :-> a class method is bound to the class & receives the class as it's first argument rather than an instance of that class. 

# static methods can't access or modify the class state . they are generally used to create utility functions that perform a task in isolation.

class Person:
    name = "anonymous"

    def change_name(self,name):
        self.name = name

p1 = Person()
p1.change_name("John")
print(p1.name) # This will print "John" because we are changing the name of the instance p1

print(Person.name) # This will print "anonymous" because we are not changing the class variable name 
# vo diff hai because we are changing the instance variable name of p1 object not the class variable name of Person class

# So to change this thing we have multiple ways to do this :->

# Way 01 . 

class Person:
    name = "anonymous"

    def change_name(self,name):
        Person.name = name

p1 = Person()
p1.change_name("John")
print(p1.name) # this will also print "John" because we are changing the class variable name of Person class
print(Person.name) # This will print "John" because we are changing the class variable name of Person class

# Way 02 .

class Person:
    name = "anonymous"

    def change_name(self,name):
        self.__class__.name = name # Yha p hamne self object ke class ko access kr lia and class variable name ko change kr dia

p1 = Person()
p1.change_name("John")

# Way 03 .

# Agr ham chahte h ke ham change_name method kk andar he class variable ko directly access kr paye so we have to use @classmethod

class Person:
    name = "anonymous"

    @classmethod # This is decorator .. 
    def change_name(cls, name):
        cls.name = name

p1 = Person()
p1.change_name("John")
print(p1.name) # This will print "John" because we are changing the class variable name of Person class
print(Person.name) # This will print "John" because we are changing the class variable name of Person class

# So now we have learned about three types of methods in python classes :-> 1. Instance method 2. Class method 3. Static method

# 1. instance method (self) :-> when we have to access the instance variables and methods of the class then we have to use instance method (self) ..
# 2. class method (cls) :-> when we have to access the class variables and methods of the class then we have to use class method (cls) ..
# 3. static method :-> when we have to create utility functions that perform a task in isolation then we have to use static method ..we dont use cls or self in static method because we dont want to access the class or instance variables and methods of the class ..