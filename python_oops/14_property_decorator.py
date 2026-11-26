# Property Decorator :-> Property decorator is used on any method in the class to use the method as a property of the class .. 

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

student1 = Student(90, 80, 70)
print(student1.percentage) # This will print the percentage of student1 object

student1.phy = 86
print(student1.phy) # Yha par changed marks print honge physics ke which is 86 .
print(student1.percentage) # Yha par percentage same he rhega phle vala , because vo phle calculate ho chuka hh .. 

# So yha par percentage ke koi fixed value nhi rkh skte . uski value baki attributes par bhi depend krti h jaise (phy, chem, math) 
# So to solve this problem we have to use property decorator ..

# Way 01 to fix this ..

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def calculate_percentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

student2 = Student(90, 80, 70)
print(student2.percentage) # This will print the percentage of student2 object

student2.phy = 86
student2.calculate_percentage() # Yha par hamne calculate_percentage method ko call kiya ..
print(student2.percentage) # Yha par percentage change ho chuka h because hamne calculate_percentage method ko call kiya jisse percentage dobara calculate ho gya ..

# Way 02 :-> Isi chiz ko krne ke simple way h property decorator ka use krna ..

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # Jo bhi method ke upar @property decorator lagaya jata h vo method ko property bana deta h ..
    # Jo bhi ye function ek value return krega vo property (attribute) m convert ho jayegi .. 
    # Ab kyuki ye function (method) h ek to ye jab bhi call hoga to latest values kk hisab ss percentage calculate krega ..
    # and ham isko access kr payenge as a property (attribute) of the class ..
    @property 
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

student3 = Student(90, 80, 70)
print(student3.percentage) # This will print the percentage of student3 object

student3.phy = 86
print(student3.percentage) # Yha par percentage change ho chuka h because hamne @property decorator ka use kiya jisse percentage dobara calculate ho gya ..