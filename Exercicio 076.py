#Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
#sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Caderno', 25.60, 'Lápis', 0.50, 'Caneta', 1.50, 'Borracha', 2.40,
            'Tesoura', 3.50, 'Cola', 2.50, 'Corretivo', 4.20,
            'Apontador', 1.50, 'Bolsa', 135.90)
print('TABELA DE PREÇOS')
print('='*35)
for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<25}', end=' ')
    else:
        print(f'R${produtos[pos]:.2f}')