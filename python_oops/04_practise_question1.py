
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
        

s1 = Student("Atul", [70, 80, 95])

avg_marks = s1.calc_avg()
print("Average Marks for this student : ", avg_marks)