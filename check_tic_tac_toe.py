import random

def check_column(temp, num):
    if (temp[0][0] == num and temp[1][0] == num and temp[2][0] == num):
        return True
    elif (temp[0][1] == num and temp[1][1] == num and temp[2][1] == num):
        return True
    elif (temp[0][2] == num and temp[1][2] == num and temp[2][2] == num):
        return True
    else:
        return False

def check_row(temp, num):
    if (temp[0][0] == num and temp[0][1] == num and temp[0][2] == num):
        return True
    elif (temp[1][0] == num and temp[1][1] == num and temp[1][2] == num):
        return True
    elif (temp[2][0] == num and temp[2][1] == num and temp[2][2] == num):
        return True
    else:
        return False

def check_diagonal(temp, num):
    if (temp[0][0] == num and temp[1][1] == num and temp[2][2] == num):
        return True
    elif (temp[0][2] == num and temp[1][1] == num and temp[2][0] == num):
        return True
    else:
        return False

def check_board(temp_b):
    print (temp_b[0])
    print (temp_b[1])
    print (temp_b[2])
    win1 = False
    win2 = False
    
    if(check_column(temp_b, 1) or check_row(temp_b, 1) or check_diagonal(temp_b, 1)):
        win1 = True
    if(check_column(temp_b, 2) or check_row(temp_b, 2) or check_diagonal(temp_b, 2)):
        win2 = True
        
    if(win1):
        print ("Player one wins.")
    elif(win2):
        print ("Player two wins.")
    else:
        print ("Draw.")


if __name__ == "__main__":
    
    winner_is_2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
    winner_is_1 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
    winner_is_also_1 = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
    no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
    also_no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]

    check_board(winner_is_2)
    check_board(winner_is_1)
    check_board(winner_is_also_1)
    check_board(no_winner)
    check_board(also_no_winner)
    
