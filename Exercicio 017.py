"""Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa"""
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca) #Para calcular a hipotenusa
print('A hipotenusa é {:.2f}'.format(hi))
