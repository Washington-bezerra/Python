#Faça um programa que leia nome e media deum aluno, guardado também a situação em um dicionario.
#no final mostre o conteudo da estrutura na tela
aluno = {'nome': '', 'media': '', 'situação': ''}

nome = str(input("Digite o nome do aluno: "))
aluno["nome"] = nome
media = float(input("Digite a media: "))
aluno["media"] = media

if media < 7:
    aluno["situação"] = "Reprovado"
else:
    aluno["situação"] = "Aprovado"

print(f'====DADOS DO ALUNO====')
for k, v in aluno.items():
    print(f'{k} = {v}')