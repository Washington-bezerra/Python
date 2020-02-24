#Faca um programa que tenha uma função chamada contador(). Que recebe tres parâmetros: inicio, fim e passo e realize a contagem. A) de 1 até 10, de 1 em 1 -- B)de 10 até 0, de 2 em 2 C)uma contagem personalizada

def contador(inicio, fim, passo):
    print('-=' * 17)

    if inicio < fim:
        if passo == 0:
            passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for cont in range(inicio, fim + 1, passo):
            print(cont, end=' ')
        print('FIM!')
    elif inicio > fim:
        if passo == 0:
            passo = 1
        if passo < 0:
            passo = passo*-1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for cont in range(inicio, fim-1, (passo*(-1))):
            print(cont, end=' ')
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 17)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim:    ')), int(input('Passo:  ')))