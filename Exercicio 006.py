#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite qualquer numero: '))

print("Analisando o numero {}\nO dobro é {}\nO triplo é {}\nE a raiz quadrada é {}".format(num, (num*2), (num*3), (num**(1/2))))