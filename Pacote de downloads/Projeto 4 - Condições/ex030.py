from time import sleep
numero = int(input('Escolha um número inteiro qualquer: '))
resultado = numero % 2
print('Processando...')
sleep(2)
if resultado == 0:
    print('O número escolhido é par, pois o seu resto é zero!')
else:
    print('Que pena! Este número é ímpar, pois o resultado é {} e portanto não tem resto igual a zero'.format(resultado))






