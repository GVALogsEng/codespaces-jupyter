
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

def argmax(array):
    index = 0

    for i in range(len(array)):
        if array[i] > array[index]:
            index = i

    return index



