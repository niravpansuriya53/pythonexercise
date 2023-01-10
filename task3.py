'''
3. You are given a list of sentences. Create a word tree from each sentence and find how many times the word is appeared in other word trees.
 Input:
sentences = `[“My name is Ram”, “”He is a good person”, “You should be careful while coding”, “He can do better”, “The person is mysterious”, “Jay Shree Ram”, “It is my pen.”]`
 Output:
word_trees = [[“My”, “name”, “is”, “Ram”], [“He”, “is”, “a”, “good”, “person”], [“You”, “should”, “be”, “careful”, “while”, “coding”], [“He”, “can”, “do”, “better”], [“The”, “person”, “is”, “mysterious”], [“Jay”, “Shree”, “Ram”], [“It”, “is”, “my”, “pen”]]
Number of time each word appears:
{“My”: 1, “name”: 1, “is”: 4, “Ram”: 2, “He”: 2, “good”: 1, “person”: 2, “You”: 1 ......} Likewise all word should be covered.
'''
# List
sentences = ["My name is Ram","He is a good person","You should be careful while coding","He can do better","The person is mysterious","Jay Shree Ram","It is my pen"]

#list of list 
list_of_list= []
for element in sentences:
    sub = element.split(', ')
    list_of_list.append(sub)    
print(list_of_list)

#list of list of string
list_of_string=[]
for list_string in list_of_list:
    for string_split in list_string:
        convert= string_split.split(' ')
        list_of_string.append(convert)
print(list_of_string)

#list of list of string convcert to one list
flat_list = []
for sublist in list_of_string:
    for item in sublist:
        flat_list.append(item)
print(flat_list)

#Count the word
from collections import Counter
count_word=Counter(flat_list)
print(dict(count_word.most_common(100000)))
#output
'''
{'is': 4, 'Ram': 2, 'He': 2, 'person': 2, 'My': 1, 'name': 1, 'a': 1, 'good': 1, 'You': 1, 'should': 1, 'be': 1, 'careful': 1,'while': 1,
  'coding': 1, 'can': 1, 'do': 1, 'better': 1, 'The': 1, 'mysterious': 1, 'Jay': 1, 'Shree': 1, 'It': 1, 'my': 1, 'pen': 1}
'''
