import random

a = []
b = []

for x in range(0,random.randrange(1,20)):
    a.append(random.randrange(1,20))

for y in range(0,random.randrange(1,20)):
    b.append(random.randrange(1,20))

a.sort()
b.sort()

print (a)
print (b)

new_list_a = [a_element for a_element in a if a_element in b]
print (new_list_a)
new_list_b = [b_element for b_element in b if b_element in a]
print (new_list_b)

"""for elem in new_list_compare:
    if new_list_compare.count(elem)>1:
        new_list_compare.remove(elem)

print (new_list_compare)

new_list_limit = []
for each in new_list_compare:
    count_a = a.count(each)
    count_b = b.count(each)
    for times in range(1,min(count_a,count_b)+1):
        new_list_limit.append(each)

print (new_list_limit)"""
    
