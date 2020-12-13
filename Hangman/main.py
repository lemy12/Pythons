import random


def pick_random_word():
    with open('sowpods.txt', 'r') as f:
        lines = f.readlines()
        number = random.randint(0, len(lines)-1)
        word = lines[number]
    return word


if __name__ == '__main__':
    print(pick_random_word())
