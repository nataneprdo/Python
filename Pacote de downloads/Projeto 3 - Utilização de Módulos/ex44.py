compras = float(input('Qual o valor das compras:'))
dinheiro = compras - (compras * 10/100)
cartão = compras - (compras * 5/100)
parcelado2 = compras / 2
parcelado3 = compras + (compras * 20/100)
print('''''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro ou pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''''')
opção = int(input('Qual é a opção:'))
if opção == 1:
    print('O valor da sua compra será de R${:.2f} com 10% de desconto'.format(dinheiro))
elif opção == 2:
    print('O valor da sua compra em será de R${:.2f} com 5%  de desconto'.format(cartão))
elif opção == 3:
    print('O valor da sua compra em 2x será de R${:.2f} mensais sem juros'.format(parcelado2))
elif opção == 4:
    totalp = int(input('Em quantas parcelas?'))
    parcela = parcelado3 / totalp
    print('O valor será de R${:.2f} em R${:.2f} mensais dividido em {} parcelas com juros'.format(parcelado3, parcela, totalp))
else:
    print('Opção inválida!')

