#Aprimore i desafio anterior, mostrando no final
#A)A soma de todos os valores pares digitados
#B)A soma dos valores da terceira coluna
#C)O maior valor da segunda linha
matriz = [list(), list(), list()]
pares = linhadois = cont = colunatres = 0
for linha in range(len(matriz)):
    for coluna in range(0,3):
        matriz[linha].append(int(input(f'Digite um valor {[linha,coluna]}: ')))
print('=-'*14)
for l in matriz:
    cont = cont + 1
    for c in range(0,3):
        print(f'[ {l[c]} ]', end='')
        if l[c] % 2 == 0:
            pares = pares + l[c]
        if cont == 2:
            linhadois = l[c] + linhadois
        if c == 2:
            colunatres = l[c] + colunatres
    print('\n')
print('=-'*14)
print(f'Soma dos valores pares: {pares}')
print(f'A soma da 3 coluna é: {colunatres}')
print(f'A soma da 2 linha é: {linhadois}')

