from random import randint
item = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''VAMOS JOGAR JOKENPÔ??? Escolha entre as opções abaixo:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Escolha uma opção:'))
print('O computador jogou {}'.format(item[computador]))
print('Você jogou {}'.format(item[jogador]))
if computador == 0:
    if jogador == computador:
        print('Empatou, jogue novamente!')
    elif jogador == 1:
        print('Você ganhou, pois PAPEL ganha de PEDRA')
    elif jogador == 2:
        print('Você perdeu, pois TESOURA ganha de PEDRA')
elif computador == 1:
    if jogador == 0:
        print('Você perdeu, pois PAPEL ganha de PEDRA')
    elif jogador == computador:
        print('Empatou, jogue novamente!')
    elif jogador == 2:
        print('Você ganhou, pois TESOURA ganha de PAPEL')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou, pois PEDRA ganha de TESOURA')
    elif jogador == 1:
        print('Você perdeu, pois TESOURA ganha de PAPEL')
    elif jogador == computador:
        print('Empatou, jogue novamente!')







