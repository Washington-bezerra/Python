import datetime
#Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTEr
ano = int(input('Ano de nascimento: '))
idade = (datetime.date.today().year - ano)
if idade <= 9:
    categoria = 'MIRIM'
elif idade <=14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade > 20:
    categoria = 'SENIOR'
print('A categoria do atleta é: {}, pois a idade dele é {}.'.format(categoria, idade))

