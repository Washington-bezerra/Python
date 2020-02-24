#Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
#digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
#a soma entre elas (desconsiderando o flag).
n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    cont += 1
    soma = soma+n
print('Você digitou {} numero e a soma entre eles é: {}'.format(cont, soma))
