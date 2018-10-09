import random

def count_cb(a,b):
    cows = 0
    bulls = 0
    for i in range(0,4):
        if(a[i]==b[i]):
            cows+=1
        elif(a.find(b[i])>=0):
            bulls+=1
    return cows, bulls

if __name__ == "__main__":
    number = str(random.randrange(1000,9999))
    count_c = 0
    count_b = 0
    guesses = 0

    while(count_c<4):
        guess = input("Enter number: ")
        while(len(guess)!=4 or not guess.isdigit() or guess.startswith('0')):
            print ("Your guess must be a 4-digit number")
            guess = input("Enter number: ")
        count_c, count_b = count_cb(number, guess)
        guesses+=1
        print (str(count_c) + " cows, " + str(count_b) + " bulls")

    print ("Congratulations, it took you " + str(guesses) + " guesses")
