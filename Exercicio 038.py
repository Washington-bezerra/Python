#Python 038: Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
pri = int(input('Digite um valor: '))
seg = int(input('Digite um segundo valor: '))
if pri > seg:
    print('O PRIMEIRO numero é maior')
elif pri < seg:
    print('O SEGUNDO é maior')
else:
    print('Os numero são iguais')