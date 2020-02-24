#Faça um programa que tenha uma lista chamada e duas funções chamadas sorteio() e SomaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
lista = list()
def sorteia():
    lista = []
    for c in range(0,5):
        lista.append(randint(0, 20))
    print(f'Os valores sorteados: {lista}')
    return lista


lista = sorteia()
#sorteia()
def somaPar(*lista):
    par = 0
    for c in lista:
        if c % 2 == 0:
            par += c
    print(f'Somando os valores pares de {lista}, temos {par}')


somaPar(*lista)