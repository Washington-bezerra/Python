#Exercício Python 008: Escreva um programa que leia um valor em metros e o
# exiba convertido em centímetros e milímetros.
valor = float(input('Digite o valor em metro: '))
km = valor/1000
cm = valor*100
mm = valor*1000
print('{}Km\n{:.0f}Cm\n{:.0f}Mm'.format(km, cm, mm))