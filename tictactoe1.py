def create_x_h(x):
    for i in range(0, x):
        print (" ---", end="")
    print ("")

def create_x_v(x):
    for i in range(0, x):
        print ("|   ", end="")
    print ("|")

def create_y(x,y):
    for j in range(0, y):
        create_x_h(x)
        create_x_v(x)

if __name__ == "__main__":
    input_x = int(input("Enter number of columns: "))
    input_y = int(input("Enter number of rows: "))
    create_y(input_x,input_y)
    create_x_h(input_x)

