import random

a = []
b = []

for x in range(1,random.randrange(1,20)):
    a.append(random.randrange(1,20))

for y in range(1,random.randrange(1,20)):
    b.append(random.randrange(1,20))

a.sort()
b.sort()

print (a)
print (b)

for a_each in a:
    for b_each in b:
        if(a_each==b_each):
            print (a_each)
            b.pop(b.index(b_each))
            break
