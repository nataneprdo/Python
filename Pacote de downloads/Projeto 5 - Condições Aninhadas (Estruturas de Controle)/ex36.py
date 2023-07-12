casa = float(input('Digite o valor da casa R$:'))
salario = float(input('Agora digite quanto é o seu salário R$:'))
anos = int(input('Em quantos anos será realizado o pagamento:'))
parcela = casa // (anos * 12)
p = salario * 30/100
print('A casa no valor de R${:.2f} parcelado {} anos será de R${:.2f} por mês.'.format(casa, anos, parcela))
if parcela <= p:
    print('Seu empréstimo foi concedido!')
else:
    print('Desculpe, mas seu empréstimo não foi concedido!')
