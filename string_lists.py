text = input("Enter a string: ")
backwards = text[::-1]

for x in range(0,len(text)):
    if(text[x]!=backwards[x]):
        print (text + " is not a palindrome")
        break
else:
    print (text + " is a palindrome")
