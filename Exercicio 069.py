#Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
#deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
contId = 0
contSX = 0
contFem = 0
while True:
    idade = int(input('IDADE: '))

    sexo = ' '.upper()
    while sexo not in 'FM':
        sexo = str(input('SEXO [F/M]: ')).upper()

    opt = ' '.upper()
    while opt not in 'SN':
        opt = str(input('Deseja continuar [S/N]: ')).upper()

    print('=-'*15)
    if sexo == 'M':
        contSX += 1

    if idade >= 18:
        contId += 1

    if sexo == 'F' and idade < 20:
        contFem += 1

    if opt == 'N':
        break
print(f'Quantiade de +18: {contId}\nQuantidade de homens: {contSX}\nQuantidade de mulheres < 20 anos: {contFem}')
