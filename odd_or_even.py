number = input("Enter number: ")
eoo = int(number)%4

if int(number)==0:
    print (number + " is a zero.")
elif eoo==0:
    print (number + " is an even number and a multiple of 4.")
elif eoo==2:
    print (number + " is an even number.")
elif eoo==1 or eoo==3:
    print (number + " is an odd number.")
