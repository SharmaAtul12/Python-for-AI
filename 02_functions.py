

#! Functions in Python

def greet():
    print("Hello, welcome to Python!")
    pass # This function does not return any value, it just prints a greeting message.

greet()  # Calling the function

temp = 35
def check_temperature():
    if temp > 30:
        print("It's a hot day.")
    else:
        print("It's a cold day.")

check_temperature()

# Working with parameters

name = "Atul"

def greet_user(name):
    print(f"Hello, {name}! Welcome to Python!")

greet_user(name)  # Calling the function with a parameter

# Returning values from functions

def add_numbers(a, b):
    return a + b  # This function returns the sum of two numbers.

result = add_numbers(5, 3)  # Calling the function and storing the result
print(f"The sum is: {result}")  # Printing the result