#Crie um programa que leia nome, sexo e idade de variass pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionarios em uma lista. No
#final, mostre:
#A)Quantas pessoas foram cadastradas.
#B)A media de idade do grupo.
#C)Uma lista com todos as mulheres.
#D)Uma lista com todas as pessoas com idade acima da media.
from typing import Dict, List, Union
pessoas = list()
dados = {}
opt = 'S'
media = 0

while opt != 'N':
    dados["Nome"] = str(input("Nome: "))
    dados["Sexo"] = str(input("Sexo [F/M]: ")).upper()
    dados["Idade"] = int(input("Idade: "))
    pessoas.append(dados.copy())
    dados.clear()
    opt = str(input("Deseja continuar [S/N]? ")).upper()
print('=-='*15)
print(f'- O grupo tem {len(pessoas)} pessoa(s)')
for p in pessoas:
    media = media + p["Idade"]
media = media/len(pessoas)
print(f'- A média de idade é de {media:.2f} anos')

print(f'- A(s) mulher(es) cadastrada(s) é(são):', end='')
for p in pessoas:
    if p["Sexo"] == 'F':
        print(f' {p["Nome"]}', end='')
print(f'\n- Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p["Idade"] > media:
        print('    => ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print('')