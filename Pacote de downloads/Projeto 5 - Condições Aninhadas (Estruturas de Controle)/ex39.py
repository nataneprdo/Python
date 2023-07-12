from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento:'))
idade = atual - ano
tempo = idade - 18
if idade > 18:
    print('Já passou da hora de se alistar pois você tem {} anos e está atrasado {} anos'.format(idade, tempo))
elif idade < 18:
    print('Fique tranquilo, ainda não está na hora de se alistar pois você tem {} e falta {} anos'.format(idade, -tempo))
elif idade == 18:
    print('Está no ano de se alistar, fique atento!')


