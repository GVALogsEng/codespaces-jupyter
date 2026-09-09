
# _____________________________________________________________________________________________

# EXAMPLE 1
# Suppose we have

# car = {
#   "brand": "Toyota",
#   "year": 2022,
#   "miles": 18000
# }

# if "brand" in car:
#  print(car["brand"])

# basic dictionary index
# "brand" in car > 'does the key "brand" exist in this dictionary?'
# car["brand"] > retrieves the value associated with "brand"

# person = {
#     "name": "Sarah",
#     "age": 24,
#     "city": "Seattle"
# }

# if "name" in person:
#     print(person["name"])
# _____________________________________________________________________________________________

# EXERCISE 2: Indexing 

# temperatures = [72, 75, 68, 79, 82]
# print(temperatures[0])  # Output: 72
# print(temperatures[1:4])  # Output: [75, 68, 79]
# _____________________________________________________________________________________________

# EXERCISE 3: Dictionary Containing a List

# students = {
#     "Chris": {
#         "age": 20,
#         "scores": [82, 91, 76]
#     },
#     "Sarah": {
#         "age": 21, # gets Sarah's dictionary
#         "scores": [95, 88, 92]
#     }
# }

# if "Sarah" in students: # Sarah is a key in the students dictionary now
#     if students["Sarah"]["scores"][1] > 85:
#         print("Sarah passed")

# or

# if "Sarah" in students and students["Sarah"]["scores"][1] > 85:
#    print("Sarah passed")

# Chained Comparisons e.g.,
# if x = 3 and y = 4
# 1 <= x + y <= 10

# simple while loop
# x = 0
# while x < 3:
#     print(x)
#     x += 1

# Why x += 1 is important
# This is shorthand for x = x + 1. It stores the value and runs until x >= 3.

# _____________________________________________________________________________________________
# EXERCISE 4: 1.4 from Textbook

# Suppose ; Also, python evaluates 'and' from Left to Right 
# data = ["A", "B", "C", "D", "E", "X"]
# j = 0

# while j < len(data) and data[j] != 'X':
#     j += 1

# print(j)  # Output: 5

# _____________________________________________________________________________________________

# EXAMPLE 5: Summation

# data = [5, 10, 20]
# total = 0
# for val in data:
#     total += val

# print(total)  # Output: 35

# Sometimes we need the index instead of the value though.

# EXAMPLE 6: maximum-index

# data = [50, 90, 70]
# big_index = 0
# for j in range(len(data)):
#     if data[j] > data[big_index]:
# we can see data[big_index] is data[0] which is 50
# Eventually, the loop reaches j = 1, and data[1] is 90, 
# which is greater than data[0] (50), so we update big_index to 1, becoming 90 > 50
# This is the fundamental algorithmic idea
#        big_index = j

# EXAMPLE 6: break / continue 

# numbers = [4, 7, 12, 19]
# for number in numbers:
#     if number == 12:
#        break / continue; will stop the loop at 12 and not print it or skip it to 19
#     print(number)

# _____________________________________________________________________________________________

# EXERCISE 5: 

# data = [14, 37, 22, 51, 43]
# big_index = 0
# for j in range(len(data)):
#     if data[j] > data[big_index]:
#         big_index = j
# print(big_index)  # Output: 3

# _____________________________________________________________________________________________

# SECTION 1.5: Functions

# Return Statement e.g.,

# def contains(data, target):
#     for item in target:
#         if item == target:
#             return True
#     return False

# 1.5.1 Information Passing

# # 'a' and 'b' are FORMAL PARAMETERS (placeholders)
# def add_numbers(a, b):
#     return a + b

# x = 10
# y = 20

# 'x' and 'y' are ACTUAL PARAMETERS (the real data)
# result = add_numbers(x, y) 

# Mutable Parameters e.g., 

# A mutable object is an object that can be changed after it is created. 
# Lists and dictionaries are mutable objects in Python. 
# When a mutable object is passed as a parameter to a function, 
# the function can modify the original object.

# grades = ["A", "B", "C"]
# grades[1] = "A"  # This changes the second element of the list to "A"
# print(grades)  # Output: ['A', 'A', 'C']

# def add_grade(data):
#     data.append("F")

# inside the function we call it "data" but outside the function we call it "grades"

#grades = ["A", "B", "C"]

# the formal parameter "data" is a reference to the actual parameter "grades"

# add_grade(grades)
# print(grades)  # Output: ['A', 'A', 'C', 'F']

# _____________________________________________________________________________________________

# EXAMPLE 6: 

# This function is meant to take a list of numbers and multiply each number by a given factor.

# def scale(data, factor):
#     for j in range(len(data)):
#         data[j] *= factor

# numbers = [10, 20, 30]

# scale(numbers, 2)
# print(numbers)  # Output: [20, 40, 60]

# _____________________________________________________________________________________________

# HOMEWORK #1 Notes

# class Pet:

#     def __init__(self, name, species, age, tricks):
#         self.name = name
#         self.species = species
#         self.__age = age
#         self.tricks = tricks

#     def introduce(self):
#         return "Hi, my name is " + self.name + ". I am a " + self.species + "."


# pet1 = Pet("Milo", "dog", 4, ["sit"])
# pet2 = Pet("Lucy", "cat", 7, ["jump"])

# print(pet1.introduce())
# print(pet2.introduce())

# _____________________________________________________________________________________________

# QUIZ PREP #1 Notes

#****
# Recall python built in type methods (Called on Objects) e.g., 
# String Methods, List Methods, Dictionary Methods

#****
# Recall python built in functions (Global) e.g., 
# Mathematics & Sequences, Iterables & Functional Programming, Type Conversion, Input & Output, Object Introspection

#****
# numbers = [1, 2, 3, 4, 5]
# len(numbers)
# len is the built-in function and numbers is the argument
# numbers.append(5)
# calling append method on object numbers
# print(len(numbers))  # Output: 6

#****
# Pythons built in types
# MUTABLE                  IMMUTABLE

# list [1, 2, 3]           int 80
# set  {1, 2, 3}           float 1.23
# dict {"name": "Alice"}   bool TRUE/FALSE
# ***KEY VALUE MAPPING     str "xxx"
#                          tuple (1, 2, 3)
#                          frozenset __

# aliases are two or more variables that refer to the same object in memory.
# e.g., a = [1, 2, 3]
#       b = a
# now supposed we do b.append(4)
# both a and b will refer to the same list object in memory, so both will be updated to [1, 2, 3, 4].
# therefore print(a) will output [1, 2, 3, 4] and print(b) will also output [1, 2, 3, 4].

# a is b    TRUE because they refer to the same object in memory.
# a == b    TRUE because they have the same value.
# now say a = [1, 2, 3]     b = [1, 2, 3]
# a is b  FALSE because they refer to different objects in memory.
# a == b  TRUE because they have the same value.

# Other example of Dic
# student = {"name": "Milo", "age": 4}
# print(student["name"])  # Output: Milo

# Type Conversion e.g.,
# int(3.14)  # Output: 3
# int(-3.9) # Output: -3
# float(2)  # Output: 2.0
# float("3.14")  # Output: 3.14
# list("hello")  # Output: ['h', 'e', 'l', 'l', 'o']

# Operators e.g.,

# Arithmetic Operators
# +    addition
# -    subtraction
# *    multiplication
# /    true division
# //   integer/floor division
# %    remainder/modulo
# **   exponentiation

# 7 / 2    # 3.5
# 7 // 2   # 3
# 7 % 2    # 1
# 2 ** 3   # 8

# Comparison Operatorse.g., 
# <  <=  >  >=  ==  !=
# Produces Boolean values (True or False) based on the comparison of two values.

# Logical Operators e.g.,
# and  or  not
# AND: one False is enough to know the result is False.
# OR:  one True is enough to know the result is True.
# NOT: negates the boolean value.

# ***
# Membership Operators e.g.,
# x in sequence
# x not in sequence
# e.g., 
# 3 in [1, 2, 3]  # True
# 7 not in [1, 2, 3]  # True

# ***
# Sequence indexing and slicing e.g., 
# a = [10, 20, 30, 40, 50]
# a[0]  # 10
# a[1:4]  # [20, 30, 40]

# bool([]) # converts/evaluates something as a boolean value, empty list evaluates to False
# empty container is False, non-empty container is True (because the list is full vs. empty)

# ***
# Control Flow e.g.,

# score = 85
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("C")

# Indentation matters e.g.,
# the colon begins the mody and intendation indicates the block of code that belongs to that control structure.

# age = 21
# if age >= 21:
#     print("allowed")
#     print("welcome")
# print("Finished")

# while loop e.g.,
# x = 1
# while x < 5:
#     print(x)
#     x += 1

# for loop e.g., 
# x = 1
# for x in range(1, 5):
#     print(x)
#     x += 1

# data = [10, 20, 30]
# for val in data:
#     print(val)

# break vs continue e.g., 
# for x in [1, 2, 3, 4]
#     if x == 3:
#         break  # stops the loop entirely
#     print(x)

# ***
# Function parameters + multable objects e.g., 

# def change(data):
#     data.append(4)
# numbers = [1, 2, 3]
# change(numbers)
# print(numbers)

# e.g., trap (doesn't change numebrs because it just reassigns the identifier data)
# def change(data):
#     data = [100, 200]
# 
# numbers = [1, 2, 3]
# change(numbers)

# print(numbers)

# ***

# scale1 vs scale2 lecture problem

# def scale1(data, factor):
#     for index in range(len(data)):
#         # j is an identifier being used to represent the current index. k, j, i are common.
#         data[index] *= factor
#         # data[index] *= factor
#         # modifies the positions inside the list

# data1 = [2,3,4]
# print(data1)
# scale1(data1,5)
# print(data1)

# because integers are immutable, we're doing val = val * 20. val → 40, but list [2, 3, 4] remains.
# we've lost the connection to the position in the list that needs replacing. 
# def scale2(data, factor):
#     for val in data:
#         val *= factor

# data2 = [2,3,4]
# scale2(data2,20)
# print(data2)

# _____________________________________________________________________________________________

# Practice Problem: Apply a Discount

# 1. Go through every INDEX in the list.
# 2. Access the element at that index.
# 3. Subtract amount from that element.
# 4. Store the result back into that position.

def discount(prices, amount):
    for index in range(len(prices)):
        prices[index] -= amount 

prices = [100, 50, 80, 20]
discount(prices, 10)
print(prices)

