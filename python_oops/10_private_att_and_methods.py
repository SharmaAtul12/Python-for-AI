# Private (like) attributes and methods in Python :->
# Private attributes and methods to be used only within the class and not accessible from outside the class. 

class Account:
    def __init__(self, acc_no, acc_passwd):
        self.acc_no = acc_no
        self.__acc_passwd = acc_passwd # to make this attribute private we use double underscore before the attribute name

    def reset_password(self, new_passwd):
        self.__acc_passwd = new_passwd # class ke andar se private attribute ko access kr skte h .. 

acc1 = Account(123456, "abc@123")

print(acc1.acc_no)   # This is public attribute and can be accessed from outside the class.
print(acc1.__acc_passwd)  # This will raise an AttributeError because __acc_passwd is a private attribute and cannot be accessed from outside the class.


class Person:
    __name = "John"  # private attribute

    # ye ham bnate h private taki koi class ke andar ka he koi method isko access kr paye .. class k bahar koi nhi access kr paye ..
    def __hello(self):  # private method
        print(f"Hello, my name is {self.__name}")

    def welcome(self):
        self.__hello()  # class ke andar se private method ko access kr skte h ..

