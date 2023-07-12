import math
ang = float(input('Digite um ângulo que você deseja:'))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem o seno {:.2f}'. format(ang, seno))
print('O ângulo de {} tem o cosseno {:.2f}'.format(ang, cosseno))
print('O ângulo de {} tem a tangente {:.2f}'.format(ang, tangente))



