'''
Find how many number of times the substring occurs in the given string.
 Input:
string = “PQRQRQRQ” 
substring = “QRQ”
 Output: 3
'''
def count_substring(string, substring):
    count = 0
    start = 0
    while start < len(string):
        positon = string.find(substring, start)
        if positon != -1:
            start = positon + 1
            count += 1
        else:
            break
    return count
# Driver Code
string = "PQRQRQRQ"
substring = "QRQ"
print(count_substring(string, substring))