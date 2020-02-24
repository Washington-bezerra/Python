#Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
# Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    situacao = 'ABAIXO DO PESO'
elif imc > 18.5 and imc <=25:
    situacao = 'PESO IDEAL'
elif imc > 25 and imc <=30:
    situacao = 'SOBREPESO'
elif imc >30 and imc <=40:
    situacao = 'OBESIDADE'
elif imc > 40:
    situacao = 'O BESIDADE MORBIDA'
print('Seu IMC é {:.1f}, por tanto sua situação é: {}'.format(imc, situacao))
