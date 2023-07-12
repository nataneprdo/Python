rota = float(input('Qual é a distância da viagem a ser percorrida em km?'))
print('Humm, a distância a ser percorrida é de {}Km...'.format(rota))
if rota <= 200:
    preço = rota * 0.50
else:
    preço = rota * 0.45
print('O valor da sua passagem será de R${}0'.format(preço))


