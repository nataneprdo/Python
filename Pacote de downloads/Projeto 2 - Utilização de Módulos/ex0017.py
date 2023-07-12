import math
cat1 = float(input('Comprimento do cateto oposto:'))
cat2 = float(input('Comprimento do cateto adjacente:'))
hip = (cat1 ** 2 + cat2 ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'. format (hip, math.sqrt(hip)))
