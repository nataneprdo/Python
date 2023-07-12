r1 = float(input('Qual é o comprimento da primeira reta:'))
r2 = float(input('Qual é o comprimento da segunda reta:'))
r3 = float(input('Qual é o comprimento da terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem sim formar um triângulo.')
    if r1 == r2 == r3:
        print('Eles formam um triângulo Equilátero!')
    elif r1 == r2 != r3 != r1:
        print('Eles formam um triângulo Escaleno!')
    else:
        print('Eles formam um triângulo Isósceles!')
else:
    print('As retas não podem formar um triângulo.')





