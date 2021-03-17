from random import randint

lista_losowa = [randint(0, 100) for x in range(10)]
lista_losowa.sort()

print(lista_losowa)

parzyste = [x for x in lista_losowa if x%2==0]
print(parzyste)