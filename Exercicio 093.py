#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
#partidas ele jogou. Depois vai ler a quantidaade de gols feitos em cada partida. No final, tudo isso será guardado em um
#dicionario, incluindo o total de gols feitos durante o campeonato.
jogador = {}
cont = 1
dados = list()
gol2 = 0
jogador["nome"] = str(input("Nome do Jogador: "))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
while len(dados) < partidas:
    gol = int(input(f'Quantos gols na partida {len(dados)+1}? '))
    dados.append(gol)
    gol2 = gol2 + gol
    cont+=1
jogador['gols'] = dados
jogador['total'] = gol2
print(f'=-='*20, f'\n{jogador}')
print(f'=-='*20)
for k in jogador.items():
    print(f'No campo {k[0]} temos o valor {k[1]}')
print(f'=-='*20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
cont = 1
while cont <= partidas:
    print(f'    =>Na partida {cont}, fez {dados[cont-1]} gol(s)')
    cont+=1
print(f'Foi um total de {jogador["total"]} gol(s)')