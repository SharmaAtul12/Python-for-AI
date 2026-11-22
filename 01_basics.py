
#! Variables ->  are used to store data values.

name = "Atul"
age = 25

#! Comments -> are used to explain the code and make it more readable. 
# This is a single line comment
""" This is a multi-line comment """

#! Data Types in Python

# 1. Integer
value = 25 - 5

# 2. Float
float_value = 25.5 + 5.5

# 3. String
first_name = "Hello"
last_name = "World"

full_name = first_name + " " + last_name

long_dash = "-" * 20

len(long_dash)  # This will return the length of the string

# 4. Boolean

is_logged_in = True
is_admin = False

num = 10

less_than_20 = num < 20  # This will return True

#! Operators in Python

age = 25
has_license = True

# and operator 

can_drive = age >= 18 and has_license  # This will return True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

#! String Manipulation

# fstrings -> this is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. It is same as Template literals in JavaScript.

name = "Atul"
age = 22

introduction = f"My name is {name} and I am {age} years old."

#! String Methods 

text = "Programming is fun"

text.lower()  # converts the string to lowercase
text.upper()  # converts the string to uppercase
text.title()  # converts the string to title case
text.startswith("P")  # checks if the string starts with "P" and returns True or False

#! Control Flow in Python 

temperature = 30

if temperature > 25: 
    print("It's a hot day")
else:
    print("It's a cold day")


#! Loops in Python


# For loop -> is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.

for i in range(5):  # range(5) generates a sequence of numbers from 0 to 4
    print(i)  # prints the current number in the loop

for i in range(1, 6):  # range(1, 6) generates a sequence of numbers from 1 to 5
    print(i)  # prints the current number in the loop

for i in range(1, 11, 2):  # range(1, 11, 2) generates a sequence of odd numbers from 1 to 10 (1, 3, 5, 7, 9)
    print(i)  # prints the current number in the loop

#! Data Structures in Python

# Lists -> are used to store multiple items in a single variable. Lists are ordered, changeable (Mutable), and allow duplicate values.

has_phone = True
my_list = [1,2, "Alice", "Bob", True, 3.14, has_phone]  # This is a list that contains different data types

my_list[0]  # This will return the first item in the list (1)
my_list[1]  # This will return the second item in the list (2)
my_list[2]  # This will return the third item in the list ("Alice")

has_phone = my_list[-1]  # This will return the last item in the list (True)

# Slicing -> is used to access a range of items in a list. It allows you to extract a portion of the list by specifying the start and end indices.
print(my_list[1:4])  # This will return a new list containing the items from index 1 to index 3 (["Bob", True, 3.14])

my_list.append("Charlie")  # This will add "Charlie" to the end of the list
my_list.remove("Alice")  # This will remove "Alice" from the list
