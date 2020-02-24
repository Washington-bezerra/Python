#Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos
#jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
from time import sleep
palpites = []
valor = cont = 0
print('=-'*17)
qtd = int(input('Quantos jogos deseja sortear? '))
print('=-=-=-= SORTEANDO SEU JOGO =-=-=-=')
while cont < qtd:
    cont+= 1
    while len(palpites) < 6:
        valor = randint(1, 60)
        if valor not in palpites:
            palpites.append(valor)
    palpites.sort()
    print(f'Jogo {cont}: {palpites}')
    sleep(1/2) #1/2 significa 0,5 segundos
    palpites.clear()
print(f'='*10, f'BOA $$ORTE!', f'='*11)