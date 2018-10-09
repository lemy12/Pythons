number = int(input("Enter number: "))


for x in range(1,1+number//2):
    if(number%x==0):
        print (x)
print (number)
