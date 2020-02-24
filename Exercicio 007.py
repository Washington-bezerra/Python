#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno
# calcule e mostre a sua média.
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

print('A media entra {} e {}, é {:.2f}'.format(nota1, nota2, (nota1+nota2)/2))
