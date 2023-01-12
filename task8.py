'''
8. You are given a list of numbers and your task is to sort the list without any inbuilt method of python.
 Input:
numbers = [2, 5, 6, 1, 3, 8, 9, 10]
 Output:
[1, 2, 3, 5, 6, 8, 9, 10]
'''

numbers=[2, 5, 6, 1, 3, 8, 9, 10]
# List sorting using bubble sort
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("sorted list using bubble sort :- ",numbers)

'''
## swaping without 3rd variable 
numbers[i] = numbers[i] + numbers[j]
numbers[j] = numbers[i] - numbers[j]
numbers[i] = numbers[i] - numbers[j]
# '''

