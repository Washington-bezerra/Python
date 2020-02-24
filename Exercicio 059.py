# Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))
ops = 0
while ops != 5:

    print('''=======================
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
=======================''')
    ops = int(input('>>>Sua opçãp: '))

    if ops== 1:
        print('A SOMA DE {} E {} É IGUAL A: {}'.format(n1, n2, (n1+n2)))
    elif ops== 2:
        print('A MULTIPICAÇÃO DE {} X {} É IGUA A: {}'.format(n1, n2,(n1+n2)))
    elif ops== 3:
        if n1 > n2:
            print('O NUMERO {} É MAIOR'.format(n1))
        elif n2 > n1:
            print('O NUMERO {} É  MAIOR'.format(n2))
        elif n1 == n2:
            print('OS NUMEROS SÃO IGUAIS')
    elif ops== 4:
        print('DIGITE OS NUMEROS NOVAMENTE...')
        n1 = float(input('Valor 1: '))
        n2 = float(input('Valor 2: '))
    elif ops== 5:
        print('>>>>>  PROGRAMA FINALIZADO   <<<<<<')

