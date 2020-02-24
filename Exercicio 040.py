# Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2
if media < 5.0:
    situa = 'REPROVADO!'
elif media > 5.0 and media < 6.9:
    situa = 'de RECUPERAÇÃO!'
elif media > 7.0:
    situa = 'APROVADO!'
print('A media é {}\nAluno está {}'.format(media, situa))
