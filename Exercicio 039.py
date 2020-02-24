#Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
#do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
nasc = int(input('Seu ano de nascimento: '))
ano = datetime.date.today().year
alist = ano-nasc
if alist > 19:
    print("Voce deve ser alista imediatamente!\nDeveria ter se alistado no ano de {}".format(nasc+18))
elif alist == 18:
    print('Voce deve se alistar esse ano ({})'.format(ano))
elif alist < 18:
    print('voce vai ser aista no ano de {}'.format(nasc+18))
