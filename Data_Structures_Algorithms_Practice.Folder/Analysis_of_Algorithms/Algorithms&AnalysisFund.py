
# The key question is "How fast is your Algorithm?"
# e.g. of factors, Power consumption? Memory usage? Time to complete?

# "How can we describe an algorithm's efficiency independently of the particular computer running it?"
# As the amount of input grows, how much additional work does the algorithm have to perform?"

# "How many seconds did this take?" to "How many basic pieces of work did this algorithm perform?"

# The lecture counts approximately two operations:
# array[0] "Access the array"
# return "return the value"

# What exactly is n? It's the size of the input. 
# if the input is [3, 6, 4, 7, 1], then n = 5 (five elements), still 2 operations

# def argmax(array):
#     index = 0
# 
#     for i in range(len(array)):
#         if array[i] > array[index]:
#             index = i
# 
#     return index

# "What work is repeated, and how does the number of repititions depend on n"

# The for loop goes through the entire array. 
# So if n = 5, the loop runs about 5 times. IF n = 100, it runs about 100 times. 

# T(n) = amount of work performed for an input of size n
# For large n, the n term deominates, so the algorithm grows like n. 
# n^2 dominates any algorithm with n, because n^2 eventually overwhelms n and constants. 

# THE SEVEN GROWTH FUNCTIONS**

#| Growth      | Core intuition                                |
#| ----------- | --------------------------------------------- |
#| 1           | same amount of work no matter n               |
#| log n       | repeatedly shrink the problem                 |
#| n           | do something once per input                   |
#| nlog n      | n items across nlogn stages                   |
#| n^2         | roughly m work for each of n items            |
#| n^3         | roughly three nested dimensions of n-work     |
#| 2^n         | possibilities explode as n increases          |

# 1 < log n < n < nlog n < n^2 < n^3 < 2^n

# e.g., 
# while n > 1:
#   n //= 2
# is O(log n)

# What is Big-O? It's just the way of naming the important growth behavior. 
# e.g., 
# 6n + 2 -> O(n)
# 4n^2 + 7n + 100 -> O(n^2)
# 20log n + 5 -> O(log n)

# Keep the fastest-growing term and remove its constant
# e.g., 7n^2 + 20n^2 + 4n + 100 -> O(n^3)

#__________________________________________________________________________________

# Reading Big-O directly from code

# for i in range(n):
#     print(i)
# Runs n times: O(n)

# for i in range(n):
#   for j in range(n):
#       print(i, j)
# Two nested n-loops. For each of n outer iterations, do n inner iterations:
# n . n = n^2 -> O(n^2)

# for i in range(n):
#     for j in range(25):
#         print(i, j)
# n . 25 = 25n -> O(n)

# while n > 1:
#   n //= 2
# O(log n)

# for i in range(n):
#     x = n
#     while x > 1:
#         x //= 2
# is n . log n -> O(nlog n)



