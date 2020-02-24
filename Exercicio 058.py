#Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
#necessários para vencer.
from random import randint
tot = 0
print('Ola, sou seu computador vou pensar num numero de  0 a 10, tente adivinhar...')
pc = randint(0,10)
escolha = int(input('Sua escolha: '))
while escolha != pc:
    tot += 1
    if escolha < pc:
        print('-*-' * 10)
        escolha = int(input('Escolha um numero maior: '))
    elif escolha > pc:
        print('-*-'*10)
        escolha = int(input('Escolha um numero menor: '))
print('\033[031;44mVocê ACERTOU !!!!\033[m\n\033[031;44mEm {} tentativas\033[m'.format(tot))
