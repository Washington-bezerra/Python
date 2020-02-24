import random
import time
import sys
#Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha = int(input('Sua escolha: '))
#if escolha >= 3:
while escolha > 2:
        print('***ESCOLHA INVALIDA, \033[31;31m TENTE NOVAMENTE!!\033[m***')
        escolha = int(input('Sua escolha: '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
time.sleep(1)

print('-='*12)
print('O PC escolheu: {}'.format(itens[pc]))
print('O jogador escolheu: {}'.format(itens[escolha]))
print('-='*12)

if pc == 0:
    if escolha ==0:
        print('EMPATOU!')
    elif escolha ==1:
        print('VC GANHOU')
    elif escolha ==2:
        print('PC GANHOU')

if pc == 1:
    if escolha == 0:
        print('PC GANHOU')
    elif escolha == 1:
        print('EMPATOU!')
    elif escolha == 2:
        print('VC GANHOU!')

if pc == 2:
    if escolha == 0:
        print('VC GANHOU')
    elif escolha == 1:
        print('PC GANHOU')
    elif escolha == 2:
        print('EMPATOU!')

print('=-'*12)