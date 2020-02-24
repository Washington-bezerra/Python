#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
#A) quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os numeros pares.
v1 = int(input('Digite valor 1:'))
v2 = int(input('Digite valor 2:'))
v3 = int(input('Digite valor 3:'))
v4 = int(input('Digite valor 4:'))
valores = (v1, v2, v3, v4)
cont = 0
i = 0
while i <= 3:
    if valores[i] == 9:
        cont = cont + 1
    i = i + 1
print('=-' * 20)
i=0 #zera o contador
while i <= 3:
    if valores[i] % 2 == 0:
        print(f'O numero {valores[i]} é par')
    i = i + 1

print(f'O numero 9 aparece {cont} vezes.')
i=0
while i <= 3:
    if valores[i] == 3:
        print(f'O numero 3 aparece na {valores.index(3)+1}ª posição')
        break
    i = i + 1
