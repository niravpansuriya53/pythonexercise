'''
11. Here you are given two series input one is arithmetic progression (A.P.) and another one is geometric progress (G.P.). In which, one of the terms is wrong. Your task is to find out the wrong term and replace it with correct term.
 Arithmetic progression: An arithmetic sequence is a sequence of numbers where the differences between every two consecutive terms is the same.
For example: 1, 2, 3, 4, 5, 6, 7, 8 is an A.P. as consecutive terms difference (2-1 = 3-2 = 4-3 = 5-4 = 6-5 = 7-6 = 8-7 = 1) is equal.
 index progression:
 Input:
One term wrong A.P. = [2, 5, 8, 11, 15, 17] One term wrong G.P. = [3, 9, 27, 81, 244, 729]
 Output:
Correct A.P. = [2, 5, 8, 11, 14, 17] Correct G.P. = [3, 9, 27, 81, 243, 729]
 '''
from collections import Counter
# Arithmetic
arithmetic_progression = [2, 5, 8, 11, 15, 17, 21]
dif_between_a_p = [arithmetic_progression[i+1] - arithmetic_progression[i] for i in range(len(arithmetic_progression)-1)]
#fetch most commne difference number
count_num = Counter(dif_between_a_p)
most_feq_number = dict(count_num.most_common(1))
a_p_num = list(most_feq_number)

for i in range(len(arithmetic_progression)-1):
    if arithmetic_progression[i+1] - a_p_num[0] != arithmetic_progression[i]:
        arithmetic_progression[i+1] = arithmetic_progression[i] + a_p_num[0]
print(arithmetic_progression)


#Geometric
geometric_progression= [3, 9, 27, 81, 244, 729]
div_between_g_p = [geometric_progression[i+1] / geometric_progression[i] for i in range(len(geometric_progression)-1)]
#fetch most comman divided
count_num = Counter(div_between_g_p)
most_feq_number = dict(count_num.most_common(1))
g_p_num = list(most_feq_number) 

for i in range(len(geometric_progression)-1):
    if geometric_progression[i+1] / g_p_num[0] != geometric_progression[0]:
        geometric_progression[i+1] = int(g_p_num[0]) * int(geometric_progression[i])
print(geometric_progression)

