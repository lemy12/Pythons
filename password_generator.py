import string, random

letters = string.ascii_letters
digits = string.digits
chars = "!@#$%^&*()-_=+[{]};:'\"\|,<.>/?"

letters_len = len(letters)
digits_len = len(digits)
chars_len = len(chars)

length = int(input("Enter length of password: "))

password = []
for x in range(1, length+1):
    if x%3==0:
        password.append(chars[random.randint(0,chars_len-1)])
    elif x%2==0:
        password.append(digits[random.randint(0,digits_len-1)])
    else:
        password.append(letters[random.randint(0,letters_len-1)])
        
print (password)
random.shuffle(password)
print (password)
password = ''.join(password)
print (password)
