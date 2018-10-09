def check_if_lower():
    num = int(input("Enter number: "))
    if num<1:
        print ("Numbers lower than 1 are not prime numbers")
        return check_if_lower()
    else:
        return int(num)

def create_range(num):
    return (number//2)+1

def dividers_list(num):
    temp = []
    for x in range (1,create_range(num)):
        if num%x==0:
            temp.append(x)
    temp.append(num)
    return temp

def print_list(num, nums):
    print ("Dividers: ", nums)
    if len(nums)>2:
        print ("Number %i is a not a prime number" % num)
    else:
        print ("Number %i is a a prime number" % num)

number = check_if_lower()
dividers = dividers_list(number)
print_list(number, dividers)

