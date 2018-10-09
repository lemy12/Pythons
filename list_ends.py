import random

def only_firstlast(lst):
    temp = []
    temp.append(lst[0])
    temp.append(lst[len(lst)-1])
    return temp

numbers = []
for x in range(1,random.randint(1,20)):
    numbers.append(random.randint(1,100))
print (numbers)

new = only_firstlast(numbers)
print (new)
