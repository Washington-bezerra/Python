#Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        print('{} '.format(c), end=' ')
        tot += 1
    else:
        print('\033[031m', end=' ')
        print('{} '.format(c), end=' ')
print('\n\033[mO NUMERO {}, FOI DIVIDIDO {} VEZES'.format(num, tot))
print('=-='*10)
if tot == 2:
    print('O NUMERO {} \033[31mÉ PRIMO!'.format(num))
else:
    print('O NUMERO {} \033[31mNÃO É PRIMO!'.format(num))
