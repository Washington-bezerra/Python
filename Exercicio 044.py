#Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('LOJAS BAGULHO DOIDO'))
preco = float(input('Qual o valor do produto: R$ '))
print('''Qual a forma de pagamento
[ 1 ] DINHERO/CHEQUE
[ 2 ] Á VISTA cartão
[ 3 ] ATÉ 2X CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
ops = int(input('Qual opção: '))
if ops == 1:
    print('VALOR FINAL {:.2f}\nDESCONTO: {:.2f}'.format(preco*0.90, preco*0.10))
elif ops == 2:
    print('VALOR FINAL: {:.2f}\nDESCONTO: {:.2f}'.format(preco*0.95, preco*0.05))
elif ops == 3:

    print('Sua compra de {:.2f}, sera parcelada em 2x de {:.2f}'.format(preco, preco / 2))
elif ops ==  4:
    parcela = int(input('Numero de parcelas: '))
    precof = preco + (preco*0.20)
    qntparc = precof / parcela
    print('Ficará {:.2f} parcela(s) de {:.2f} cada\nVALOR FINAL C/ JUROS: {:.2f}'.format(parcela, qntparc, precof))
else:
    print('\033[0;30;41mOPÇÃO DE PAGAMENTO INVALIDA, TENTE NOVAMENTE')