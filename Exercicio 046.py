#Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
# artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for cont in range(10, -1, -1): #1º -1 = para ir até 0; 2ª -1 = para a contagem ser regressiva
    print(cont)
    sleep(0)
print("\ncabuuuum")
