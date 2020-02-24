#Crie um programa onde o usuario possa digitar sete valores numerico e cadastre-os em uma lista unica que mantenha separados os
#valores pares e impares. no final mostre os valores pares e impares em ordem crescente
numeros = [list(), list()]
for c in range (1,8):
    num = int(input(f'Digite o {c}º numero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('='*30)
print(f'Os numeros pares são: {numeros[0]}')
print(f'Os numeros impres são: {numeros[1]}')