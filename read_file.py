names_dict = {}

with open("nameslist.txt","r") as open_file:
    line = open_file.readline().strip('\n')
    while line:
        if line in names_dict:
            names_dict[line] = names_dict[line] +1
            line = open_file.readline().strip('\n')
        else:
            names_dict[line]=1
            line = open_file.readline().strip('\n')

print (names_dict)
