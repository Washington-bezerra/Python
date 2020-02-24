#Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Qual o valor do produto: '))
desc = produto*0.95

print('O produto que custava R${:.2f}, na promoção com 5% de desc. sai por R${:.2f}!'.format(produto, desc))