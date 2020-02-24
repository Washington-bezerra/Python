#Faça um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostra qual foi o maior e o
#menor valor digitado e as suas respectivas posições na lista.
valores = []
maior = 0
menor = 0
for v in range(0,5):
    valores.append(int(input(f'Digite o valor da posição {v}: ')))
    if v == 0:
        maior = valores[v]
        menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]

print('=*'*35)
print(f'Você digitou os seguinte numeros: {valores}')
print(f'O maior valor é {maior} e ele está na(S) posição(es): ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor é {menor} e ele está na(s) posição(es): ', end='')
for i,v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
print()
