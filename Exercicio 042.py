#Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
print('-=-'*20)
print('ANALISADOR DE TRIANGULO')
print('-=-'*20)
r1 = float(input('Digite o lado 1: '))
r2 = float(input('Digite o lado 2: '))
r3 = float(input('Digite o lado 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('Com essas medidas forma um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    if r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Não forma triangulo')