
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


