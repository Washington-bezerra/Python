#Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
#os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
#digitar valores.
ops = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while ops != 'N':
    n = int(input('Digite um numero: '))
    ops = str(input('Deseja continuar [S/N]: ')).strip().upper()

    cont += 1
    soma = soma + n
    if cont == 1:
        maior = n
        menor = n
    elif cont != 1:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('VOCE DIGITOU {} NUMERO E A MEDIA É {}'.format(cont, (soma/cont)))
print('MAIOR NUMERO: {}\nMENOR NUMERO: {}'.format(maior, menor))

