a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

number = input("Enter number: ")
for each in a:
    if each<int(number):
        b.append(each)

print (b)
