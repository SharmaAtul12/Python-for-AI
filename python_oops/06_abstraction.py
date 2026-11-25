# Abstraction : Hiding the implementation details of a class and only showing the essential features to the user. It helps in reducing programming complexity and effort.
# Unnecessary details , jinki zrurt nhi hai user ko . unko hide krne ka process hi abstraction hai .

# Ex : In a car , user ko sirf steering , break , accelerator ka use karna aata hai . baki engine kaise work krta hai ye user ko nhi pta hota .



class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False

    # User ko sirf start method ka use karna aata hai . baki implementation details user ko nhi pta hota .
    # Usko bs dikha ke Car Started ....  ho gya hai . baki self.clutch = True , self.acc = True ye implementation details user ko nhi pta hota .
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started .... ")

car1 = Car()
car1.start()