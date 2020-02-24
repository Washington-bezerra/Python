#faça um programa que tenha um função, que receba as dimensões de um terreno retangular (altura e comprimento) e mostre a área do terreno.
print(f'  CONTROLE DE TERRENO', f'\n', f'-'*22)
def terreno(a, b):
    print(f'A área de um terreno {a} x {b} é de {a*b}m²')


a = float(input(f'ALTURA (m): '))
b = float(input(f'COMPRIMENTO (m): '))
terreno(a, b)
