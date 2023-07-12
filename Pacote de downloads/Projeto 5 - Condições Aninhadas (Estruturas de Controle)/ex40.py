nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
média = (nota1 + nota2) / 2
if média < 5.0:
    print('Você foi reprovado pois sua média foi de {}'.format(média))
elif média >= 5.0 and média < 7:
    print('Você está de recuperação pois sua média foi de {}'.format(média))
elif média >= 7.0:
    print('Você foi aprovado pois sua média foi de {}'.format(média))