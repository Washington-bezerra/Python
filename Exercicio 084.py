#Faça um programa que leia nome e peso de vários pessoas guardando tudo em uma lista. No final, mostre:
#A)Quantas pessoas foram cadastrada
#B)Uma listagem com as pessoas mais pesadas
#C)Uma listagem com as pessoas mais leves
maiorpeso = menorpeso = 0
pessoas = list()
principal = []
while True:
    pessoas.append(str(input('NOME: ')))
    pessoas.append(float(input('PESO: ')))
    opt = str(input('Deseja continuar? [S/N] ')).upper()
    if len(principal) == 0:
        maiorpeso = pessoas[1]
        menorpeso = pessoas[1]
    else:
        if maiorpeso > pessoas[1]:
            maiorpeso = pessoas[1]

        if menorpeso < pessoas[1]:
            menorpeso = pessoas[1]
    principal.append(pessoas[:])
    pessoas.clear()
    while opt not in 'SN':
        opt = str(input('Deseja continuar? [S/N] ')).upper()
    if opt == 'N':
        break
print('=*'*20)
print(f'Total = {len(principal)}')
print(f'O maior peso foi {maiorpeso}, pessoa(s) -> ', end='')
for cont in principal:
    if cont[1] == maiorpeso:
        print(f'{cont[0]}')
print(f'O menor peso foi {menorpeso}, pessoa(s) -> ', end='')
for cont in principal:
    if cont[1] == menorpeso:
        print(f'{cont[0]}')