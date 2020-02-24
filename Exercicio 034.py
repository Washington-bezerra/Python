# Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# . Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Digite seu salario: '))
if sal>=1250.00:
    aumento = sal+(sal*0.10)
if sal<1250.00:
    aumento = sal+(sal*0.15)
print('Seu salario será: R${:.2f}'.format(aumento))