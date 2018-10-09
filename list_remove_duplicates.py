import random

lst = []
for x in range(1,random.randint(2,20)):
    lst.append(random.randint(2,20))

lst.sort()
print (lst)

lst_set = []
for each in lst:
    if each not in lst_set:
        lst_set.append(each)

print (lst_set)
