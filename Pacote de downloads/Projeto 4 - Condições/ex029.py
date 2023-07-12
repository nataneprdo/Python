velocidade = int(input('Digite a velocidade em que o carro está:'))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Sua velocidade está em {}km/h e você foi multado, o valor da sua multa é R${},00.'.format(velocidade, multa))
else:
    print('Você não foi multado!')