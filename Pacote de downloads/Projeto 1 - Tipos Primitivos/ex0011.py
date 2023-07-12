largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} , sua área é de {}m² e'. format(largura, altura, area))
tinta = area / 2
print('você utilizar {}l de tinta em {}m².'. format (tinta, area))


