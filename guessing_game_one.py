import random

number = random.randint(1,9)
number_of_guesses = 0
while True:
    number_of_guesses += 1
    guess = int(input("Enter your guess: "))
    if(guess > number):
        print ("Your guess was too high")
    elif(guess < number):
        print ("Your guess was too low")
    else:
        print ("You have guessed the number")
        if(number_of_guesses == 1):
            print("It took you 1 guess, nice")
        else:
            print ("It took you %i guesses" % number_of_guesses)
        break
