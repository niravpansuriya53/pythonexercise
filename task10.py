"""
Print the following patterns. In the patterns ‘_’ (underscore) denotes the space. **_**
"""
# input
n = int(input("Enetr a number :- "))

"""
1.
    ** **
    *   *
        
    *   *
    ** **
"""


def diamond(n):
    for row in range(1, n + 1):
        row = row - (n // 2 + 1)
        if row < 0:
            row = -row
        print("*" * row + " " * (n - row * 2) + "*" * row)
    print()


"""
2.
      *  
     *** 
    *****
     *** 
      *  
"""


def space_diamond(n):
    for row in range(1, n + 1):
        row = row - (n // 2 + 1)
        if row < 0:
            row = -row
        print(" " * row + "*" * (n - row * 2) + " " * row)
    print()


# call diamond and space_diamond
if n % 2 == 0:
    n = n - 1
    diamond(n)
    space_diamond(n)
else:
    diamond(n)
    space_diamond(n)

"""
3.
    *
    **
    * *
    *  *
    *   *
    ******
"""
for row in range(1, n + 1):
    for col in range(row):
        if col == 0 or col == row - 1:
            print("*", end="")
        else:
            if row != n:
                print(" ", end="")
            else:
                print("*", end="")
    print()
print()

"""
4.
    *****
    *   *
    *   *
    *   *
    *****
"""
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

"""
5.
    1 
    2 3 
    4 5 6 
    7 8 9 10 
    11 12 13 14 15  
"""
number = 1
for row in range(n + 1):
    for col in range(1, row + 1):
        print(number, end=" ")
        number += 1
    print()
