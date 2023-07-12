número = int(input('Digite um número para ver a sua tabuada:'))
for tab in range(0, 11):
    r = número * tab
    print('{}  x {:2} = {:3}'.format(número, tab, r))
print('FIM!')