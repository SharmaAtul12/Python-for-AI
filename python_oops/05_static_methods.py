# Static Methods -> are those methods which don't use self parameter . and they work at class level Means :->
# mm static methods ko unke class ke name ss he call kr skta hu 


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    # Decorator for static method -> Decorator is a function which takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
    # and then return a new function with extended behavior.
    @staticmethod 
    def hello():
        print("Hello Students")

    def calc_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum / len(self.marks)
        return avg
        

s1 = Student("Atul", [70, 80, 95])

avg_marks = s1.calc_avg()
print("Average Marks for this student : ", avg_marks)

s1.hello() # calling static method using object of class
Student.hello() # calling static method using class name