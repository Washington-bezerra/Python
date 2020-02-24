#Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
#até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'set',
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezaseis', 'dezasete', 'dezoito', 'dezanove', 'vinte')

while True:
    num = int(input('Digite um numero de 0 a 20: '))
    if num >= 0 and num <= 20:
        break
    print('TEENTE NOVAMENTE. ', end=' ')
print(f'Você digitou o numero => {numero[num]}')
