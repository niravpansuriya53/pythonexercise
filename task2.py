# Person names
names = [
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
]
#Create dictionary name: name length
names_length = {name: len(name) for name in names}
print("Length of names :", list(names_length.values()))

# Sorting 
sorted_names_length = sorted(names_length.items(), key=lambda x: x[1])
print(sorted_names_length)

#Create dictionary name length vise value
length_wise_names = dict()
for name_length_tuple in sorted_names_length:
    if name_length_tuple[1] in length_wise_names.keys():
        length_wise_names[name_length_tuple[1]].append(name_length_tuple[0])
    else:
        length_wise_names[name_length_tuple[1]] = [name_length_tuple[0]]

# 3 most frequent names
print(" \nThe three most frequent name lenghts are:")
three_most_freq_names = dict(sorted(length_wise_names.items())[:3])
for key,value in three_most_freq_names.items():
    print(len(value)," names of length ",key ,":",value)

# 3 least frequent names
print(" \nThe three least frequent name lenghts are:")
three_least_freq_names = dict(sorted(length_wise_names.items())[-3:])
for key,value in three_least_freq_names.items():
    print(len(value)," names of length ",key ,":",value)

#output
'''
Length of names : [5, 7, 8, 5, 5, 5, 6, 6, 5, 6, 8, 6, 7, 5]
 
The three most frequent name lenghts are:
6  names of length  5 : ['Smith', 'Jones', 'Brown', 'Davis', 'Moore', 'White']
4  names of length  6 : ['Miller', 'Wilson', 'Taylor', 'Thomas']
2  names of length  7 : ['Johnson', 'Jackson']
 
The three least frequent name lenghts are:
4  names of length  6 : ['Miller', 'Wilson', 'Taylor', 'Thomas']
2  names of length  7 : ['Johnson', 'Jackson']
2  names of length  8 : ['Williams', 'Anderson']
'''