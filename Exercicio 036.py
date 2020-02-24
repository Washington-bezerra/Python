#Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa? '))
salario1 = float(input('Qual o seu salario? '))
pagar = int(input('Em quantos anos deseja pagar? '))
anos = pagar*12
salario = salario1*0.30
parcela = casa/anos
if parcela > salario:
    print('Seu emprestimo foi negado, pois o valor da parcela é maior que 30% do salário.\n'
          '30% do salario = {:.2f}\nValor da parcela: {:.2f} '.format(salario, parcela))
else:
    print('Parabens, emprestimo aprovado!!\nSerão {} parcelas, no valor de {:.2f} cada'.format(anos, parcela))
