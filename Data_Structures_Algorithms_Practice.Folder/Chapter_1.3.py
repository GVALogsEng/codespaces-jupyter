
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

