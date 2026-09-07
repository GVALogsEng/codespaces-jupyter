
September 7, 2026: Analysis of Algorithms

As 'n' increases, so does the runtime. 
During experimental studies, you will experiment with different inputs to calculate runtimes. 
In order to compare two algorithms, the same hardware and software environments must be used. 

{
Theoretical Analysis***
-- Uses a high-level description of the algorithm; we run 
-- Characterizes running time as a function of the input size, n. 

The Random Access Machine (RAM) Model <>

Elementary Operations, and each different one, takes a different amount of time in practice.
Math (), Comparisons(), Function calls and value returns, Variable assignment, Array allocation, Variable increment or decrement, etc.

EXAMPLE***
Constant Running TIme:

function first(array):
// input: an array
// output: the first element
return array[0] // returns the element at index 0 

"What is the runtime complexity?" / "How many operations are performed in this function?"
ANSWER***
It performs 2 operations. 
Ques. "What if there were 100,00 elements?" 
ANSWER*** 
It is always 2 operations. An array has N elements (input size), but will only have 2 operations.

________________________________________________________________________________________________________________________________

EXAMPLE***
Linear Running Time:

def argmax(array):
// input: an array
// Output: the index of the maximum value
index = 0    // assignment, 1 op
for i in range(len(array)):  // 1 + 1 op per loop
    if array[i] > array[index]:  //3 ops per loop
        index = i    // 1 op per loop, someties
return index     // 1 op 
# the interesting part here is the for loop. It is now iterative, and will perform the operation 'n' times. 
# Let's count the number of operations in the for loop. 

Ques. "How many operations if the list has 10 elements?" "What is the funtime?" 
ANSWER***
The total operations: T(n) = 6n + 2 (The polynomial / linear expression: this is a linear operation)
________________________________________________________________________________________________________________________________

EXAMPLE***
Estimating Running Time

Algorithm argmax executes 6n + 2 primitive. 
operations in the worst case, 5n + 2 in the best case.
<> CHECK LATER FROM SLIDE***
________________________________________________________________________________________________________________________________

EXAMPLE***
Growth Rate of Running Time

Changing the hardware / software environment 
-- Affects T(n) by a constant factor, but 
<> CHECK LATER FROM SLIDE***
________________________________________________________________________________________________________________________________

EXAMPLE***
Quadratic Running Time

Changing the hardware / software environment 
-- Affects T(n) by a constant factor, but 
<> CHECK LATER FROM SLIDE***

________________________________________________________________________________________________________________________________

EXAMPLE***
Some Common Computing Times

log(2)n / n / nlog(2)n / n^2 / 2^n

A quadratic runtime complexity is O(n²), meaning an algorithm's execution time grows proportionally to the square of the input size. 

________________________________________________________________________________________________________________________________

EXAMPLE***
Insertion Sort

import timeit
import random

def timeFunction(f,n,repeat=1):
	return timeit.timeit(f.__name__+'('+str(n)+')',setup="from __main__ import "+f.__name__,number=repeat)/repeat

def insertion_sort(data_list):
    # 1. Split data into two parts: sorted & unsorted
    #    X | X X X X X X X
    #    sorted | unsorted
    # 2. While size of unsorted part is greater than zero锛?    #   a. let the target element be the first element in the unsorted part
    #   b. find targets insertion point in the sorted part
    #   c. make place at insertion point by shifting all larger elements
    #   d. insert the target in its final, sorted position

    # Coding: Please sort the values in-place, i.e. no new data_list is created and final sorted values are in data_list
    pass

def python_sort(data_list):
    # Use list.sort()
    # Python built in sort uses Tim-sort
    pass

if __name__ == '__main__':
    data1 = []
    data2 = []
    for i in range(10000):
        value = random.randint(0,1000)
        data1.append(value)
        data2.append(value)
    print("Insertion sort 10000 elements:",
          '{:.6f}'.format(timeFunction(insertion_sort, data1)), "seconds")
    print("Built in sort 10000 elements:",
          '{:.6f}'.format(timeFunction(python_sort, data2)), "seconds")
          
def insertion_sort(data_list):
    for j in range(1, len(data_list)):
        key = data_list[j]
        i = j - 1

        while i >= 0 and data_list[i] > key:
            data_list[i + 1] = data_list[i]
            i = i - 1

        data_list[i + 1] = key


def python_sort(data_list):
    data_list.sort()

1. Treat the left part of the list as sorted.

2. Take the first element from the unsorted part.
   Call it the key.

3. Compare the key to elements on its left.

4. Any element larger than the key gets shifted right.

5. Keep moving left until the key belongs there.

6. Insert the key.

7. Repeat until the entire list is sorted.

INSERTION-SORT(A)

for j = 1 to n - 1
    # Move through the list from left to right.
    # Everything before j is treated as already sorted.

    key = A[j]
    # Save the current value we want to insert
    # into the correct place in the sorted left side.

    i = j - 1
    # Start looking immediately to the left of key.

    while i >= 0 and A[i] > key
        # Keep moving left while:
        # 1. we are still inside the list, and
        # 2. the value on the left is bigger than key.

        A[i + 1] = A[i]
        # Shift that bigger value one position to the right
        # to make room for key.

        i = i - 1
        # Move one step farther left and compare again.

    A[i + 1] = key
    # We found the correct location.
    # Put key into the open spot.
