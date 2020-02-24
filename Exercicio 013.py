#Python 013: Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento.

sal = float(input("Digite seu salario: R$"))
novo = sal + (sal*0.15)
print('Seu salario antigo: R${:.2f}\nValor do aumento: R${:.2f}\nNovo salario: R${:.2f}'.format(sal, (sal*0.15), novo))
