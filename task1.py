'''1. Create a list of 10 numbers and show the 5 different operations options to the user on screen. The 5 different operations are as following,
 A. Length of the list
 B. Display first 3 numbers
 C. Display sum of odd numbers
 D. Number of duplicate numbers
 E. Display list without duplicate numbers
 Input:
numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]
 Output:
If user select option A:
o Length of the list: 10 If user select option B:
o First 3 numbers: [2, 4, 5] If use select option C:
o Sum of odd numbers: 14 If user select option D:
o Number of duplicate numbers: 2 # (2, 5 repeats in the list) If user select option E:
o List without duplicate numbers: [2, 3, 4, 12, 44, 1, 3]
'''
number_list=[2, 4, 5, 2, 12, 44, 5, 1, 2, 3]
print(len(number_list))

#task B
print(number_list[:3])

#task C
sum=0
for i in number_list:
    if i%2 !=0:
        sum +=i
print(sum)

#task D
abc=[]
for i in number_list:
    if number_list.count(i) > 1:
        abc.append(i)
print(len(list(set(abc))))











