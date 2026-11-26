# Del keyword :-> used to delete object properties or object itself ..
# Kyuki jab ham Object create krte h to vo memory me store hota h , uske attributes and methods memory m space lete h , to agar hame us object ko delete krna h to ham del keyword ka use krte h ..

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("John")
del s1
# print(s1) This will raise an error because s1 has been deleted