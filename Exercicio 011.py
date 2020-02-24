#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
altura = float(input('Altura da parece(m): '))
largura = float(input('Largura da parece(m): '))

area = altura*largura

print('Sua parede tem a dimensão de {:.2f} X {:.2f}, portanto a areá é de {:.2f}M²'.format(altura,largura, area))
print('Você vai precisa de {:.4}L de tinta.'.format(area/2))