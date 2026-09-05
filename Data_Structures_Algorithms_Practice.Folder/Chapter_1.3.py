
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

# EXERCISE 2: Indexing 

# temperatures = [72, 75, 68, 79, 82]
# print(temperatures[0])  # Output: 72
# print(temperatures[1:4])  # Output: [75, 68, 79]

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

