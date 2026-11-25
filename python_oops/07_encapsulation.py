# Encapsulation :-> Isme ham ek capusle (single unit) bna lete h (Data + related functions(methods)) Ka ..
# So basically ek class bnana with data members and methods is Itself the process of encapsulation ..

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def calc_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum / len(self.marks)
        return avg

# So here encapsulation is done by creating a class Student which has data members name and marks and a method calc_avg() which calculates the average marks of the student. The data members and methods are encapsulated within the class Student.
s1 = Student("Alice", [85, 92, 78, 96])
print(s1.calc_avg())