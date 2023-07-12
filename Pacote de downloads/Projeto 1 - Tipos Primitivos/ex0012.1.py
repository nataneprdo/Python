preço = float(input('Qual é o preço do produto? R$'))
desc = preço - (preço * 20 / 100)
print('O valor do produto que era {}R$, com o desconto passa a custar {}R$.'. format(preço, desc))
