#Exercício Python 004: Faça um programa que leia algo
#pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print('É numero e letra => ',algo.isalnum())
print('É letra =>',algo.isalpha())
print('É maiusculo =>',algo.isupper())
print('É numero decimal =>',algo.isdecimal())
