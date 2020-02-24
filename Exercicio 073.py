#Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
#de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
brasileirao =('Atletico', 'Flamengo', 'Corinthians', 'Palmeiras', 'Fluminense', 'America-MG', 'Sao Paulo',
              'Gremio', 'Vasco da Gama', 'Internacional', 'Botafogo', 'Sport Recife', 'Cruzeiro', 'EC Vitoria', 'Santos', 'Chapecoense',
              'Atletico-PR', 'Bahia', 'Ceara SC', 'Parana')
print('='*15)
print(f'Os 5 primeiros colocados são: {brasileirao[0:5]}')
print('='*15)
print(f'Os quatro ultimos colocados: {brasileirao[-4:]}')
print('='*15)
print(f'Os times em ordem alfabetica: {sorted(brasileirao)}')
print('='*15)
print('A Chapecoense está em {}ª lugar. '.format(brasileirao.index('Chapecoense')+1))