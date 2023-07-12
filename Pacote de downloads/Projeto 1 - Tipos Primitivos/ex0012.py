preço = float(input('Qual é o valor? R$'))
desc = preço - (preço * 5 / 100)
print('O valor {}R$ custará {}R$ com 5% de desconto.'. format(preço, desc))
