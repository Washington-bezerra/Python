#Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
#usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
total = 0
barato = ''
cont = 0
menor = 0
while True:
    prod = str(input('PRODUTO: '))
    valor = float(input('VALOR: '))
    opt = ' '.upper()
    while opt not in 'SN':
        opt = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if valor > 1000.00:
        cont = cont + 1
    total += valor
    if cont == 1:
        menor = valor
        barato = prod
    else:
        if valor < menor:
            menor = valor
            barato = prod
    if opt == 'N':
        break
print(f'Total da compra: R${total:.2f}\nProdutos que custam mais de R$1000: {cont}\nNome do produto mais barato: {barato.upper()}')