'''
13. Create a class name Number with the following methods.
# Starter code
Class Number:
def __init__(self, numbers)
self.numbers = numbers
def get(self):
# Your code that returns the list which we set during initialization
def change_original_values(self, func: lambda x: x): # func has default value # Use python map() here
new_numbers = [] # your code, apply passed function here
return new_numbers
def filter_values(self, filter_func: lambda x: x)
# Use python filter() here
filtered_numbers = [] # Your code, apply passed function here return filtered_numbers
def compound_the_numbers(self, reduce_func: lambda compound, d: compound + d): # Use python reduce() here: terminal function that returns single value compounded
by reduce_func
compounded_value = Your code, apply passed function here return compounded_value
def sort(self):
# Sort the list and return sorted list return sorted_list
if __name__ == “__main__”: numbers = [2, 5, 1, 66, 22, 11, 10]
# Create an object of Number class and initialize it. n1 = Number(numbers)
# Print the list print(“Numbers: ”, n1.get())
# lambda_func1 = Create lambda function that doubles the value of list print(“New values:”, n1.change_original_values(func=lambda_func1))
# lambda func2 = Create lambda function that filter out odd numbers print(“Filtered values:”, n1.filter_values(filter_func=lambda_func2))
# lambda_func3 = Create lambda function to pass as reduce_function print(“Compounded value:”, n1.compound_the_numbers(reduce_func=lambda_func3))
# Sort the list
print(“Sorted list:”, n1.sort())
 Output:
Numbers: [2, 5, 1, 66, 22, 11, 10] New values: [4, 10, 2, 132, 44, 22, 20] Filtered values: [2, 66, 22, 10] Compounded value: 117
Sorted list: [1, 2, 5, 10, 11, 22, 66]
'''
from functools import reduce
class Number:

    #initialization
    def __init__(self, numbers):
        self.numbers = numbers

    #Get values
    def get(self):
        return f'Numbers: {self.numbers}'

    #Doubles the value of list
    def change_original_values(self, func = lambda x: x):
        return  list(map(func, self.numbers))

    #Filter values
    def filter_values(self, func: lambda x: x):
        return list(filter(func, self.numbers))

    #Sum of list
    def compound_the_numbers(self, reduce_func: lambda compound, d: compound + d):
        return reduce(reduce_func, self.numbers)

    #sorting the list
    def sort(self):
        return sorted(self.numbers)



if __name__ == "__main__":
    numbers = [2, 5, 1, 66, 22, 11, 10]
    #create object
    n1 = Number(numbers)
    print(n1.get())

    #call change value
    func1 = lambda x: x*2
    print("New values:", n1.change_original_values(func1))

    #Filtere values
    func2 = lambda x: x%2 == 0
    print("Filtered values:", n1.filter_values(func2))

    #Sum is list
    func3 = lambda x, y: x+y
    print("Compounded value:", n1.compound_the_numbers(func3))

    #sorting the list
    print("Sorted list:", n1.sort())
