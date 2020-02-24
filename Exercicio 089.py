#Crie um programa que leia nome e duas notas de carios alunos e guarde tudo em uma lista composta. No final mostre o um boletim
#contendo a média de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.
alunos = []
dados = []
opt = 'S'
numeroaluno = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota1: ')))
    dados.append(float(input('Nota2: ')))
    alunos.append(dados[:])
    dados.clear()
    opt = str(input('Dejase continuar ? [S/N]')).upper()
    while opt[0] not in 'SN':
        opt = str(input('Dejase continuar ? [S/N]')).upper()
    if opt[0] == 'N':
        break
print('=-'*15)
print(f'No. ', f'Nome         ', f'Média')
print(f'-----'*6)
for a in range(len(alunos)):
    print(f'{a}   ', f'{alunos[a][0]:<13}', f'{(alunos[a][1]+alunos[a][2])/2}')
print('=-'*25)
numeroaluno = int(input('Mostrar nota de qual aluno (999 interrompe): '))
if numeroaluno > len(alunos):
    print(f'O ALUNO NÃO EXISTE')
    while numeroaluno >= len(alunos):
        numeroaluno = int(input('***Mostrar nota de qual aluno (999 interrompe): '))
        if numeroaluno < len(alunos):
            break
        print(f'*O ALUNO NÃO EXISTE\n**************************')
while numeroaluno != 999:
    if numeroaluno > len(alunos):
        print(f'O ALUNO NÃO EXISTE')
        while numeroaluno >= len(alunos):
            numeroaluno = int(input('***Mostrar nota de qual aluno (999 interrompe): '))
            if numeroaluno < len(alunos):
                break
            print(f'*O ALUNO NÃO EXISTE\n**************************')

    print(f'Notas de {alunos[numeroaluno][0]}:  >{alunos[numeroaluno][1]} e {alunos[numeroaluno][2]}<')
    print('-'*13)
    numeroaluno = int(input('Mostrar nota de qual aluno? (999 interrompe)'))
