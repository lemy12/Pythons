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


def check_board(temp_b, num):
    print(temp_b[0])
    print(temp_b[1])
    print(temp_b[2])

    win1 = False
    win2 = False

    if num == 1:
        if check_column(temp_b, "O") or check_row(temp_b, "O") or check_diagonal(temp_b, "O"):
            win1 = True
    else:
        if check_column(temp_b, "X") or check_row(temp_b, "X") or check_diagonal(temp_b, "X"):
            win2 = True

    if win1:
        print("Player one wins.")
        return True
    elif win2:
        print("Player two wins.")
        return True
    elif '-' not in temp_b[0] and '-' not in temp_b[1] and '-' not in temp_b[2]:
        print("Draw.")
        return True
    else:
        return False


def ask_player(board, num):
    if num == 1:
        print("Player one, where to put O?")
    else:
        print("Player two, where to put X?")

    choice = input().split(',')
    choice[0] = int(choice[0])
    choice[1] = int(choice[1])

    while board[choice[0]-1][choice[1]-1] != '-':
        print("Choose blank spot")
        choice = input().split(',')

    if num == 1:
        board[choice[0]-1][choice[1]-1] = "O"
    else:
        board[choice[0]-1][choice[1]-1] = "X"

    return board


if __name__ == "__main__":
    currentBoard = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    isItOver = False

    while True:
        currentBoard = ask_player(currentBoard, 1)
        if check_board(currentBoard, 1): break
        currentBoard = ask_player(currentBoard, 2)
        if check_board(currentBoard, 2): break
