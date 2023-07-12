from time import sleep
a = float(input('Digite o primeiro valor:'))
b = float(input('Digite o segundo valor:'))
print('Processando...')
sleep(3)
if a > b:
    print('O primeiro valor é maior.')
elif b > a:
    print('O segundo valor é maior.')
elif a == b:
    print('Não existe valor maior pois ambos são iguais.')
print('Fim!')