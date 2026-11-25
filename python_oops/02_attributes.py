# Attributes in Python are variables that belong to an object or class. They can be used to store data and define the state of an object. There are two main types of attributes: instance attributes and class attributes.
# We have Two types of attributes in Python:
# 1. Class Attributes: Jo Class own krti hh and sabhi objects k liye same hoti hh. Class attributes are defined inside the class but outside any method. They are shared among all instances of the class.
# 2. Instance (Object) Attributes: Jo object own krta hh and har object k liye alag hoti hh. Instance attributes are defined inside the constructor (the __init__ method) and are unique to each instance of the class.

# Ex : for a class Student, the name of the student is an instance attribute because each student can have a different name. However, if we have a class attribute like school_name, it will be the same for all students.
# Generally , Instance Attributes are defined using self(which is hamrare object ka reference) keyword inside the constructor and Class Attributes are defined using any variable name outside the constructor.

class Student:
    # Class Attribute
    college_name = "ABC College"  # This is a class attribute. It is shared among all instances of the class.
    name = "anonymous" # class attribute

    def __init__(self,name,age):
        # Instance Attributes
        # When we have same name for both class attribute and instance attribute, then instance attribute will take precedence over class attribute. 
        # So Object Attribute > Class Attribute
        self.name = name  # This is an instance attribute. It is unique to each instance of the class.
        self.age = age    # This is another instance attribute. It is unique to each instance of the class.

# Creating instances of the Student class
s1 = Student("Atul", 20)
print(f"Student 1 : Name: {s1.name}, Age: {s1.age}, College: {s1.college_name}")