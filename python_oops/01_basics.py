
# Object is called Instances  
# Constructor in class -> Jab bhi object create hota hai to constructor call hota hai
# Constructor hamesha ek parameter leta hai jise hum self kehte hai. Self ka matlab hota hai ki ye object ka reference hai.
# Agr ham constructor nhi bnate hai to python khud ek default constructor bana deta hai and har object create hone par call hota hai. Constructor ka naam hamesha __init__ hota hai.
# The data which is stored inside the class (like name here ) are called attributes and the functions which are defined inside the class are called methods. The attributes and methods are collectively called as members of the class.

class Student:
    # Constructors

    # Default constructors -> Jisme sirf self parameter hota hai. Ye constructor hamesha call hota hai jab bhi object create hota hai.
    # Agr isko ham nhi bnayenge to isko python khud bana dega and har object create hone par call hota hai.
    def __init__(self):
        print("I'm the Default Constructor")

    # Parameterized constructors -> Jisme self ke alawa aur bhi parameters hote hai. Ye constructor hamesha call hota hai jab bhi object create hota hai.
    def __init__(self, name):
        print(self)
        print("Adding a new student")
        self.name = name  # self.name is an instance variable (jo object k andar new create hone vala h) and name is a passed parameter (jo constructor k andar pass ho rha h). So, self.name = name means that we are assigning the value of the passed parameter name to the instance variable self.name.


# These Parenthesis are used to call the constructor . and this s1 and self are the same object
s1 = Student("Atul")
print(s1.name)

s2 = Student("Rohit")
print(s2.name)



