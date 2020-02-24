#Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
        sexo = str(input('\033[41mOPÇÃO INVALIDA, TENTE NOVAMENTE!\033[m\nDigite seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {}, registrado com *sucesso*!'.format(sexo))
