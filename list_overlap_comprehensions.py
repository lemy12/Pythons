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

overlap = []

for x in range(1,21):
    count_a = 0
    count_b = 0
    for each in a:
        if each==x:
            count_a+=1
    for each in b:
        if each==x:
            count_b+=1
    if count_a > count_b:
        for i in range(0,count_b):
            overlap.append(x)
    else:
        for i in range(0,count_a):
            overlap.append(x)

print (overlap)
