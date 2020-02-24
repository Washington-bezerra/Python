#Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite o numero inteiro: '))
print('''Escolha uma das bases para converção:
[1] converter para BINARIO.
[2] converter para OCTAL.
[3] converter para HEXADECIMAL.''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('A converção de {} para BINARIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('A converção de {} para OCTAL {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('A converção de {} para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE.')