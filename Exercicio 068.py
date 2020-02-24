#Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
#jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
while True:
    #cont = 0
    soma = 0

    n = int(input('Digite um numero de 0 a 10: '))
    escolha = str(input('Escolha [I/P]: ')).strip() .upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Escolha [I/P]: ')).strip().upper()[0]
    pc = randint(0, 10)
    soma = n + pc
    print('=-' * 10)
    print(f'Você escolheu {n} e o PC escolheu {pc}')
    if escolha == 'P':
        if soma %2 == 0:
            print('VOCÊ GANHOU')
            cont += 1
        else:
            print('O PC ganhou.')
            break
    elif escolha == 'I':
        if soma %2 != 0:
            print('VOCÊ GANHOU')
            cont += 1
        else:
            print('O PC ganhou.')
            break
    print('=-' * 30)
    print('Vamos jogar novamente')
print('*'*10)
print(f'VOCE GANHOU {cont} vezes!')