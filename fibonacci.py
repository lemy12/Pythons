lst = [1,1]

def fibo(number, lista):
    lista.append(lista[number-1]+lista[number-2])

podaj = int(input("Enter amount: "))

for x in range(2,podaj):
    fibo(x,lst)

print (lst)
