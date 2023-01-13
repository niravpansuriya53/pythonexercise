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
# Arithmetic
arithmetic_progress= [2, 5, 8, 11, 15, 17]
for index in range(len(arithmetic_progress)-1):
    if arithmetic_progress[index] - arithmetic_progress[index+1]  != -3:
        arithmetic_progress[index+1] = arithmetic_progress[index] +3
print(arithmetic_progress)

#