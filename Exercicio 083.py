#Crie um programa onde o usuario digite uma expressão qualquer que use parentese. Seu aplicativo deverá
#analisar se a expressão passada esrá com os parenteses abertos e fechados na ordem correta.
expressao = list((str(input('Digite uma expressão: '))))
contPar = 0
valida = ''
for v in range(len(expressao)):
    if expressao[v] == '(':
        contPar += 1
    elif expressao[v] == ')':
        contPar -= 1
if contPar == 0:
    valida = 'VALIDA'
else:
    valida = 'ERRADA'
print(f'Sua expressão está {valida}')