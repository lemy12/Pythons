def guess_letter(w):

    w = w.rstrip()
    w_answer = [char for char in w]
    w_block = ["_" for x in range(0, len(w))]
    already_guess = []
    tries = 6

    while True:
        print(w_block)
        print("Tries left: ", tries)
        letter = input("Guess your letter: ").upper()
        while letter in already_guess:
            letter = input("Try different letter: ")
        already_guess.append(letter)
        if letter not in w_answer:
            tries = tries - 1
        for i in range(0,len(w_block)):
            if letter == w_answer[i]:
                w_block[i] = w_answer[i]
        if w_block == w_answer:
            print(w_block)
            print("Congratulations!")
            break
        elif tries < 1:
            print("I'm sorry, but you are out of tries.")
            break

    return input("Do you want to start another game?")


if __name__ == "__main__":
    word = "EVAPORATE"
    guess_letter(word)