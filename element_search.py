import random

def middle(lst):
    return lst[(len(lst)//2)]

def b_search(lst, num):
    print (lst)
    mid = middle(lst)
    if num==mid:
        return True
    elif len(lst)==1:
        return False
    elif num>mid:
        return b_search(lst[lst.index(mid)::],num)
    elif num<mid:
        return b_search(lst[:lst.index(mid):],num)
    
num_list = []
for x in range(1, random.randint(8,15)):
    num_list.append(random.randint(1,20))
num_list.sort()
print (num_list)

num_list = list(set(num_list))

rand_num = random.randint(1,20)
print (rand_num)

answer_bool = b_search(num_list, rand_num)

if answer_bool:
    print ("Number " + str(rand_num) + " is in the list.")
else:
    print ("Number " + str(rand_num) + " is not in the list.")
