# So In class , we can store two things : 1. Data (Attributes) 2. Functions (Methods) . so class is a collection of data and functions. 
# Ex : for a class Car : 
#      Data : color, model, price, speed, mileage
#      Functions : start(), stop(), accelerate(), brake() . so methods are functions that belongs to object . Class ke andar ke functions are called methods .

class Student:

    def __init__(self, fullname, marks):
        self.fullname = fullname
        self.marks = marks

    # Methods kk andar first parameter hamesha self hota hai. Self ka matlab hota hai ki ye object ka reference hai. Agr ham self ko method k andar nhi likhenge to python error dega.
    # But hmari mrzi hai ke isko use krna h ya nhi , but likhna zrur hai .. 
    def hello(self):
        print(f"Hello, my name is {self.fullname} and my marks are {self.marks}")

    def get_marks(self):
        return self.marks

s1 = Student("Atul", "95")
s1.hello()  # Hello, my name is Atul

marks = s1.get_marks()
print("Your marks are : ", marks)