'''
=>You are given a list of numbers and your task is to find out the pairs that have sum equals n (provided during input).
 No duplicate pair or similar pair should be in the output.  For example, if sum=12,
o [4, 8] can’t come twice in the output.
o Also, consider [4, 8] and [8, 4] as similar, so only [4, 8] have to come, not
both.
 Input:
o Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8] o n = 12
 Output:
o [[3, 9], [4, 8], [2, 10]]
See here, each pair addition is equals to 12 i.e. (3+9=12, 4+8=12, 2+10=12)
'''


from itertools import combinations
#list
numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]

#combinations of list
list_of_list=[]
pairs = list(combinations(set(numbers),2))

# pairs of sum equals number
sum_no=int(input("Enter a sum of number :- "))
list_of_sum=[]
for item in pairs:
    if sum_no == item[0]+item[1]:
        list_of_sum.append(list(item))
print(list_of_sum)

#Output
'''
Enter a sum of number :- 12
[[3, 9], [4, 8], [2, 10]]
'''
