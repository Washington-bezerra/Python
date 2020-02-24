#Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando a estrutura while.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razao da PA: '))
termo = primeiro
c = 1
while c <=10:
    print('{} > '.format(termo), end=' ')
    termo += razao
    c += 1
print('FIM')
