salario = float(input('Qual é o seu salário atual:'))
aumento1 = salario + (salario * 10/100)
aumento2 = salario + (salario * 15/100)
if salario <= 1250:
    print('O valor do salário passa a ser R${}'.format(aumento2))
else:
    print('O valor do salário passa a ser R${}'.format(aumento1))

