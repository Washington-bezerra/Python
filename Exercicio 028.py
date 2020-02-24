import random
lista = [0, 1, 2, 3, 4, 5]
escolha = random.choice(lista)

num = int(input('Estou pensando em um numero entra 0 e 5, qual é o numero? '))

if num==escolha:
    print('\nEu pensei em {}, e vc tambem, vc ganhou!!'.format(escolha))
else:
    print('\nEu pensei em {}, e vc em {}, EU GANHEI'.format(escolha,num))