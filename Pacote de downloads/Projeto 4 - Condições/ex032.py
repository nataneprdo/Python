from datetime import date
ano = int(input('Digite um ano qualquer ou coloque 0 para saber se o ano atual é bissexto:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')



