import random
cor1 = input('Digite a primeira cor:')
cor2 = input('Digite a segunda cor:')
cor3 = input('Digite a terceira cor:')
cor4 = input('Digite a quarta cor:')
lista = [cor1, cor2, cor3, cor4]
escolhida = random.choice(lista)
print('A cor escolhida foi {}'.format(escolhida))