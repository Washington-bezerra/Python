#Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
print('=*'*15)
if inverso == junto:
    print('\033[31mÉ um palíndromo.')
else:
    print('\033[31mNão\033[m é um palíndromo.')