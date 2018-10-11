names_dict = {}

with open("Training_01.txt","r") as open_file:
    line = open_file.readline()
    line_edit = line.strip('\n').split("/")
    while line:
        curr = line_edit[2]
        if curr in names_dict:
            names_dict[curr] = names_dict[curr] +1
            line = open_file.readline()
            line_edit = line.strip('\n').split("/")
        else:
            names_dict[curr] = 1
            line = open_file.readline()
            line_edit = line.strip('\n').split("/")


print (names_dict)
