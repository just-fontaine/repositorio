preco = float(input(' Qual o valor do produto? R$'))
print('\n Para descobrir o valor de acordo com a condição digite: ')
print('\n Preço à vista (dinheiro/cheque): 0'
      '\n Preço à vista (cartão): 1'
      '\n em até 2x no cartão: 2'
      '\n 3x ou mais no cartão: 3')

condicao = int(input('\n Tipo de pagamento: '))

if condicao == 0:
    print(f'\n O preço do produto à vista em dinheiro/cheque é {preco - preco * 10 / 100}.')
elif condicao == 1:
    print(f'\n O preço do produto à vista no cartão é {preco + preco - 5 / 100}')
elif condicao == 2:
    print(f'\n O preço do produto em até 2x no cartão é {preco}')
else:
    if condicao == 3:
        print(f'\n O preço em 3x ou mais no cartão é {preco + preco * 20/100}')
