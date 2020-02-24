#Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantidade de letra A na frase: {}'.format(frase.count('A')))
print('A primeira vez que aparece A: {}'.format(frase.find("A") + 1))
print('A ultima posição que A aparece: {}'.format(frase.rfind("A") + 1))
