def create_birthday_dictionary():
    dict = {}
    with open("birthday.txt") as fhandle:
        for line in fhandle:
            tempLine = line.rstrip().split()
            dict[tempLine[0]+tempLine[1]] = dict.get(tempLine[0]+tempLine[1], tempLine[2])
    return dict


if __name__ == "__main__":
    print(create_birthday_dictionary())