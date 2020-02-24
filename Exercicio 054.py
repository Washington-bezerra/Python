#Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
cont = 0
cont2 = 0
for c in range (1, 8):
    id = int(input('Data de nasc. da {}º pessoa: '.format(c)))
    idade = datetime.date.today().year - id
    if idade >= 18:
        cont += 1
    else:
        cont2 +=1
print('=*'*15)
print('Temos {} pessoas maiores de idade\nE {} pessoal menores de idade.'.format(cont, cont2))
