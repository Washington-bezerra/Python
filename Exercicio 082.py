#Crie um programa que vai ler vários números e colocar em uma lista.
#depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados.
#Ao final, mostre o conteúdo das três listas geradas
lista = []
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    opt = str(input('Deseja continuar? [S/N]')).upper()
    while opt not in 'SN':
        opt = str(input('Deseja continuar? [S/N]')).upper()
    if opt == 'N':
        break
for cont in range(0, len(lista)):
    if lista[cont] % 2 == 0:
        pares.append(lista[cont])
    else:
        impares.append(lista[cont])
print(f'=*'*20)
print(f'Lista completa: {lista}\nLista de numeros pares: {pares}\nLista de valores impares: {impares}')
