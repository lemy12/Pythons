from pick_word import pick_random_word
from guess_letters import guess_letter

if __name__ == '__main__':
    choice = "yes"
    while choice == "yes":
        choice = guess_letter(pick_random_word())