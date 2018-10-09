from datetime import date

name = input("Enter your name: ")
age = input("Enter your age: ")
number = input("Enter number: ")

now = date.today()
onehundred = int(now.year) + 100 - int(age)

for x in range(0, int(number)):
    print (name + ", in " + str(onehundred) + " you will be 100 years old.")
