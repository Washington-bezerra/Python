#Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for
num = int(input('Qual tabuada deseja? '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, (num*c)))
