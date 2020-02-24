#Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.
print('-=-'*20)
print('ANALISADOR DE TRIANGULO')
print('-=-'*20)
r1 = float(input('Digite o lado 1: '))
r2 = float(input('Digite o lado 2: '))
r3 = float(input('Digite o lado 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('Com essas medidas forma um triangulo')
else:
    print('Não forma triangulo')