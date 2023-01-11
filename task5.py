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
#sum of to number
Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
list_of_list=[]
def find(Numbers, length_of_list, sum_no):
    for i in range(length_of_list):
        for j in range(i):
            list_of_two_sum_no=[]
            if (Numbers[i] + Numbers[j]) == sum_no:
                list_of_two_sum_no.append(Numbers[i])
                list_of_two_sum_no.append(Numbers[j])
                list_of_list.append(list_of_two_sum_no)

#enter a sum ofnumber
sum_no=int(input("Enter a two number of sum:- "))

#uniq list of list
find(Numbers, len(Numbers), sum_no)
list_of_tuple_uniq = list(set(tuple(sorted(sub)) for sub in list_of_list))
list_of_list_uniq = [list(ele) for ele in list_of_tuple_uniq]
print(list_of_list_uniq)
