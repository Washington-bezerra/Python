#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario se for
#diferente de zero, o dicionario receberá também o ano de contratação e o salario. Calcule e acrescente, além da idade com
#quantos anos a pessoa vai se aposentar.
import time
dados= {}

dados["Nome"] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
dados["Idade"] = (int(time.strftime("%Y"))-nascimento)
dados["CTPS"] = int(input("CTPS (0 CASO NÃO TENHA): "))
if dados["CTPS"] != 0:
    dados["contribuição"] = int(input("Ano da 1º contribuição: "))
    dados["Aposentadoria"] = dados["Idade"]+35
    dados["Salario"] = float(input("Seu salario: R$ "))
print('=='*10)
for k,v in dados.items():
    print(f'{k} = {v}')