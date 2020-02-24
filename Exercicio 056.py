#Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.
somaid = 0
maioridade = 0
nomevelho = ''
totmuler20 = 0
for p in range (1, 5):
    print('===== {}ª ====='.format(p))
    nome = str(input('Nome: ')).strip()
    id = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaid += id
    if sexo in 'fF' and id >= 20:
        totmuler20 += 1

    if p == 1 and sexo in 'Mm':
        maioridade = id
        nomevelho = nome
    if sexo in 'mM' and id > maioridade:
        maioridade = id
        nomevelho = nome
mediaid = somaid/4
print('=-'*15)
print('A media das idade é: {:0}'.format(mediaid))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print('Mulher(es) com 20 ou mais ano de idade: {}'.format(totmuler20))
