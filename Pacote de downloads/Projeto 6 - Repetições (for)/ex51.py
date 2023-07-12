termo = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
décimo = termo + (10 - 1) * razão
for pa in range(termo,décimo + razão, razão):
    print('{}'.format(pa), end=' ->  ')
print('Acabou!')