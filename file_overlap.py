n_list_prime = []
n_list_happy = []
n_list_overlap = []

with open("primenumbers.txt","r") as open_file:
    line = open_file.readline().strip('\n')
    while line:
        n_list_prime.append(line)
        line = open_file.readline().strip('\n')

with open("happynumbers.txt","r") as open_file:
    line = open_file.readline().strip('\n')
    while line:
        n_list_happy.append(line)
        line = open_file.readline().strip('\n')

for each in n_list_prime:
    if each in n_list_happy:
        n_list_overlap.append(each)

print (n_list_overlap)
