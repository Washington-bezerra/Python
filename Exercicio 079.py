#Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
#digitados, em ordem crescente.
lista = list()

while True:
    val = int(input('Digite um valor: '))
    if val not in lista:
        lista.append(val)
        print(f'O numero foi adicionado com sucesso!')
    else:
        print(f'O valor já EXISTE na lista. ')
    opt = str(input('Deseja continuar [s/n]? '))
    while opt not in 'sn':
        opt = str(input('INVALIDO USE SOMENTE s OU n.\nDeseja continuar [s/n]? ')).lower()
    if opt in 'n':
        break
print('=-'*25)
lista.sort()
print(f'A SUA LISTA FICOU: {lista}')
