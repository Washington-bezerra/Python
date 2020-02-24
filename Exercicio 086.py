#crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lido pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = [list(), list(), list()]
for linha in range(len(matriz)):
    for coluna in range(0,3):
        matriz[linha].append(int(input(f'Digite um valor {[linha,coluna]}: ')))
print('=-'*14)
for l in matriz:
    for c in range(0,3):
        print(f'[ {l[c]} ]', end='')
    print('\n')
print('=-'*14)