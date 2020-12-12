numbers = ''
high = 0

print("Enter values: ")
numbers = input()

numbers = numbers.split(',')

for num in numbers:
    if int(num) > high:
        high = int(num)

print(high)