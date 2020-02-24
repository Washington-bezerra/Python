#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
#A)Quantos numeros foram digitados.
#B)A lista de valores ordenada de forma decrescente
#C)Se o valor 5 foi digitado e está ou não na lista.
valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    opt = str(input(f'Deseja continuar[S/N]? ')).upper()
    if opt in 'N':
        break
print('=*'*25)
print(f'FORAM DIGITADOS: {len(valores)} NUMERO(S)')
valores.sort(reverse=True)
print(f'O valor de forma inversa é: {valores}')
if 5 in valores:
    print(f'O valor 5 aparece na lista')
else:
    print(f'O valor 5  não aparece na lista')