# Polymorphism :-> ek he chiz ka alag alag form me hona ko polymorphism kehte h .. (Ek hi action, alag-alag data ke saath alag tarah kaam kare.)
# The ability of single function or method to work with different types of data and behaving differently based on the data type is called polymorphism ..

# Operator Overloading :-> ek operator ka alag alag form me hona ko operator overloading kehte h .. jaise ki + operator ka use addition, concatenation, merge etc me hota h ..

# So in sab operations mm + ka meaning alg alg h .. jaise ki addition, concatenation, merge etc .. 
# This is implicit overloading jo python nn hamare liye khud kr di , hame kuch kri ke zrurt nhi pdi .. 
print(1 + 2) # Output : 3 so yha pp + ka mtlb hai addition
print("Hello" + " World") # Output : Hello World so yha pp + ka mtlb hai concatenation
print([1, 2, 3] + [4, 5, 6]) # Output : [1, 2, 3, 4, 5, 6] so yha pp + ka mtlb hai merge

# Creating a complex number class to demonstrate operator overloading
# so yha pp + ka mtlb hai addition of complex numbers ab vo hame define krna hoag , kyuki python m to vo chiz defined nhi hh .. 

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real, "i + " , self.img , "j" )

    def add(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)

num1 = Complex(2, 3)
num1.show_number() # Output : 2 i + 3 j

num2 = Complex(4, 5)
num2.show_number() # Output : 4 i + 5 j

# Abhi ham complex no ko aise add nhi kr pa rhe -> num1 + num2 ye error dega kyuki python ko ye nhi pta ki complex no ka addition kaise krna h ..
num3 = num1.add(num2)
num3.show_number() # Output : 6 i + 8 j

# So To define this logic of addition of complex numbers using + operator , we will use dunder functions in python ..
# dunder functions :-> dunder functions are special methods in python which have double underscores at the beginning and end of their names ..



class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real, "i + " , self.img , "j" )

    # So yha par maine dunder function ka use krkr , python ko bta dia ke iss type kk data par + ka mtlb kya hh , vo addtion kaise hoga .. 
    def __add__(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)

num1 = Complex(2, 3)
num1.show_number() # Output : 2 i + 3 j

num2 = Complex(4, 5)
num2.show_number() # Output : 4 i + 5 j

# This is operator overloading because maine apne + operator ka meaning define kr diya , ki complex no ka addition kaise krna h ..
num3 = num1 + num2 # Now we can add complex numbers using + operator
num3.show_number() # Output : 6 i + 8 j

