import json


def create_birthday_dictionary():
    with open("birthday.json", "r") as fRead:
        info = json.load(fRead)
    name = input("New name: ")
    date = input("New date: ")
    info[name] = date
    with open("birthday.json", "w") as fWrite:
        json.dump(info, fWrite)
    return info


if __name__ == "__main__":
    print(create_birthday_dictionary())