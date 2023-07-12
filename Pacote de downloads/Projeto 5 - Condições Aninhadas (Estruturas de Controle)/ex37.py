num = int(input('Digite um número inteiro qualquer:'))
print('''Digite a opção de conversão desejada:
[ 1 ] Para Binário
[ 2 ] Para Octal 
[ 3 ] Para Hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('O valor {} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O valor {} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O valor {} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
print('Fim do conversor!')

