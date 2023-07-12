dia = int(input('Digite a quantidade de dias foi alugado:'))
distância = float(input('Digite os km percorridos:'))
pago = dia * 60
km = distância * 0.15
total = pago + km
print('O valor será de {}R$ por {} dias e {}km rodados.'. format (total, dia, distância))
