frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece a primeira vez em {}'.format(frase.find('A')+1))
print('A letra A aparece a última vez em {}'.format(frase.rfind('A')+1))
