#Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o valor 1: '))
b = int(input('Digite o valor 2: '))
c = int(input('Digite o valor 3: '))
#Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < a:
    menor = c
#verificando o meior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c
print('O menor numero é {}\nO maior numero é {}'.format(menor, maior))

