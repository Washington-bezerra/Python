"""Python 018: Faça um programaque leia um ângulo qualquer e mostre na tela o valor do
seno, cosseno e tangente desse ângulo."""
import math

ang = float(input('Digite um angulo: '))
seno = math.sin(math.radians(ang))
con = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print("O angulo de {}° tem\nCosseno de {:.3f}\nSeno de {:.3f}\nTangente de {:.3f}".format(ang, con, seno, tan))