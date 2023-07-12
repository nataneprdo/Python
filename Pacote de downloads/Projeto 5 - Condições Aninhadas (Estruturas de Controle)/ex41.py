from datetime import date
atual = date.today().year
ano = int(input('Digite o seu ano de nascimento:'))
idade = atual - ano
print('O atleta possui {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria é Mirim')
elif idade <= 14:
    print('Sua categoria é Infantil')
elif idade <= 19:
    print('Sua categoria é Júnior')
elif idade <= 25:
    print('Sua categoria é Sênior')
elif idade > 25:
    print('Sua categoria é Master')