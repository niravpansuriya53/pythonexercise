'''2. You are given a list of person names. Your task is to find out the three most frequent and three least frequent names.
 Input:
names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
 Output:
o Names: 'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White'] o Name lengths: [5, 7, 8, 5, 5, 5, 6, 6, 5, 6, 8, 6, clr7, 5]
o The three most frequent name lenghts are:
6 names of length 5: ['Smith', 'Jones', 'Brown', 'Davis', 'Moore'] 
4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']
2 names of length 8: ['Williams', 'Anderson']
o The three least frequent name lenghts are:
2 names of length 7: ['Johnson', 'Jackson']
2 names of length 8: ['Williams', 'Anderson']
4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']'''

names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
names1=[]
for i in names:
    len1= len(i)
    names1.append(len1)
print(names1)
from collections import Counter
counts = dict(Counter(names1))
# print(counts)

myKeys = list(counts.keys())
myKeys.sort()
sorted_dict = {i: counts[i] for i in myKeys}
print(sorted_dict)

#Finde top three most  frequent name lenght
top_three = sorted(counts, key=counts.get, reverse=True)[:3]
# print(top_three)

top_three_most=[]
for top in top_three:
    for name in names:
        if len(name) ==  top:
            top_three_most.append(name)
print(top_three_most)
print("length of 5",top_three_most[:6])
print("length of 6",top_three_most[6:10])
print("length of 7",top_three_most[10:])

last_three = sorted(counts, key=counts.get, reverse=True)[-3:]
last_three_most=[]
print(last_three)
for last in last_three:
    for name in names:
        if len(name) == last:
            last_three_most.append(name)
print(last_three_most)
print("length of 6",last_three_most[:4])
print("length of 7",last_three_most[4:6])
print("length of 6",last_three_most[6:])
