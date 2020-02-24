#Faça um programa que tenha uma função chamada maior(), Que recebe vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior
from random import randint
a = randint(0, 8)
def sorteio(a):
    lista = list()
    for c in range(0, a):
        lista.append(randint(1, 10))
    return lista

lista = list(sorteio(a))
def maior(*lista):
    maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for c in lista:
        print(f'{c}', end=' ')
        if c == 1:
            maior = c
        else:
            if c > maior:
                maior = c

    print(f'Foram informador {len(lista)} valores ao todo')
    print(f"O MAIOR É {maior}")

maior(*lista)