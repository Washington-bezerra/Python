#Python 010: Crie um programa que leia quanto
# dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Dólar comercial	R$ 3,5026 // Dólar turismo	R$ 3,6500 // Dólar ptax	R$ 3,4811
'''vlr = float(input('Digite quanto Reais vc tem: '))
dc = vlr/3.5026
dt = vlr/3.6500
dp = vlr/3.4811

print("\nCom R$ {:.2f} vc consegue adquirir\n\nU${:.2f} Dolar comercial\nU${:.2f} Dolar turismo\nU${:.2f} Dolar ptax".format(vlr, dc, dt, dp))'''

vlr = float(input("Quantos R$ você tem? "))

print('Com R$ {:.2f} você consegue adquirir:\n    Dolar comercial: {:.2f}\n    Dolar turismo: {:.2f}\n    Dolar ptax: {:.2f}'.format((vlr), (vlr/3.5026), (vlr/3.6500), (vlr/3.4811)))