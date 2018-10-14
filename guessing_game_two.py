def high_or_low(choice, lst, g):
    if choice in ["h", "high", "higher"]:
        temp = lst[lst.index(g)::]
        return temp
    elif choice in ["l", "low", "lower"]:
        temp = lst[:lst.index(g):]
        return temp
    elif choice in ["equal", "e"]:
        temp = [g]
        return temp


if __name__ == "__main__":
    
    guess_list = [x for x in range(1,101)]
    guess = guess_list[len(guess_list)//2]

    while(len(guess_list)>1):
        option = ""
        while (option not in ["h", "high", "higher", "l", "low", "lower", "equal", "e"]):
            option = input("Is your number higher, lower or equal to " + str(guess) + "?")
        guess_list = high_or_low(option, guess_list, guess)
        guess = guess_list[len(guess_list)//2]
    
    print ("Your number is " + str(guess_list[0]) + ".")
