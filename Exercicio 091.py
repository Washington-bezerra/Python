#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guade esses resultados num dicionario
#No final, coloque esse dicionario que o vencedor tirou o maior numero no dado.
from random import randint
from time import sleep
jogadores= {}
cont = 1
print(f'Valores sorteados:')
while cont <= 4:
    sorteio = randint(0,6)
    print(f'    O jogador{cont} tirou {sorteio}')
    jogadores[cont] = sorteio
    sleep(1)
    cont+= 1
print('Ranking dos jogadores:')
cont=0
for item in reversed(sorted(jogadores, key = jogadores.get)):
    cont+=1
    print(f'    {cont}º lugar: Jogador{item} com {jogadores[item]}')