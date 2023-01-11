'''
4. Recursion:
 Create a recursive function which returns the n-th Fibonacci number. [Fibonacci
sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]
o Input: N=8
o Output: 21
o Also, check if your recursive function is able to return the Fibonacci value at 60th or 90th term? If no, then check the concept of m8moization for Fibonacci in recursive way.
 Create a recursion function that calculate the sum of numbers present in the list. o Input:
numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
o Output: 152'''
#fibonacci
fib_dict = {0: 0,1: 1}
def fib(num):
    if num not in fib_dict:
        fib_dict[num] = fib(num-1) + fib(num-2)
    return fib_dict[num]
number_of_fibonacci=int(input("Enter a number :- "))
print(number_of_fibonacci,"th fibonacci is:- ",fib(number_of_fibonacci))
