def guess_letter(w):

    w_answer = [char for char in w]
    w_block = ["_" for x in range(0, len(w))]
    already_guess = []

    while True:
        print(w_block)
        letter = input("Guess your letter: ")
        while letter in already_guess:
            letter = input("Try different letter: ")
        already_guess.append(letter)
        for i in range(0,len(w_block)):
            if letter == w_answer[i]:
                w_block[i] = w_answer[i]
        if w_block == w_answer:
            print(w_block)
            print("Congratulations!")
            break


if __name__ == "__main__":
    word = "EVAPORATE"
    guess_letter(word)