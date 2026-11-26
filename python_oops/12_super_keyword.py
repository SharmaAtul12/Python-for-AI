# Super Keyword :-> used to call the parent class constructor or methods from the child class ..
# Basically it is used to access the parent class methods and properties from the child class ..
# To jab bhi ham super likh rhe hote h to vo parent class ko refer kr rha h , aur jab bhi ham super().__init__() likh rhe h to vo parent class ke constructor ko call kr rha h ..

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started ...")

    @staticmethod
    def stop():
        print("Car Stopped ...")


class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start() # This will call the start method of parent class Car

car1 = ToyotaCar("fortuner", "Diesel")
print(car1.type) # This will raise an error because type is not defined in ToyotaCar class ..(if we are not using super().__init__(type) in ToyotaCar class constructor)