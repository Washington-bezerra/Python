#Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
#quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razao da PA: '))
termo = primeiro
c = 1
mais = termo
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} > '.format(termo), end=' ')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos vc quer mostra a mais? '))
print('Fim do programa!!')
