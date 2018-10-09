while True:
    
    player_one = input("Player one choice: ")
    player_two = input("Player one choice: ")
    
    if player_one=="rock":
        if player_two=="paper":
            print ("Player two wins!")
        elif player_two=="scissors":
            print ("Player one wins!")
        else:
            print ("Draw!")
    elif player_one=="paper":
        if player_two=="scissors":
            print ("Player two wins!")
        elif player_two=="rock":
            print ("Player one wins!")
        else:
            print ("Draw!")
    if player_one=="scissors":
        if player_two=="rock":
            print ("Player two wins!")
        elif player_two=="paper":
            print ("Player one wins!")
        else:
            print ("Draw!")
    
    choice = input("Do you want to play another one?")
    if choice=="N":
        break
