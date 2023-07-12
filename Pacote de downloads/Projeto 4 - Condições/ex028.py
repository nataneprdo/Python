from random import randint
from time import sleep
computador = randint(0,5)
print('Vou pensar em um número, tente adivinhar para me vencer!')
numero = int(input('Agora digite um número entre 0 e 5:'))
print('Processando...')
sleep(3)
if numero == computador:
    print('Parabéns! Você venceu!')
else:
    print('Ops, você perdeu! Eu pensei no número {} e não no {}! Tente novamente!'.format(computador, numero))







