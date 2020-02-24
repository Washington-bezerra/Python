#Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()#para excluir os espaço no começo e no fim
print('Analisando os dados...')
print('Seu nome todo em maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome tem {} Letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} Letras'.format(nome.find(' ')))