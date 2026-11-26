class Employee:
    def __init__(self, role, dep, sal):
        self.role = role
        self.dep = dep
        self.sal = sal

    def show_details(self):
        print(f"Role: {self.role}, Department: {self.dep}, Salary: {self.sal}")

class Engineer(Employee):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "1000000")

eng1 = Engineer("Atul", "20")
eng1.show_details()
    
    