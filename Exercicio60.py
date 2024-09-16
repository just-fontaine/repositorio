total = mais_que_mil = menor = cont = maior = 0
barato = ' '
caro = ' '

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    cont += 1
    if cont == 1:
        menor = maior = preco
        barato = caro = nome
    elif preco < menor:
        menor = preco
        barato = nome
    else:
        if preco > maior:
            maior = preco
            caro = nome
    total += preco
    if preco > 1000:
        mais_que_mil += 1
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar not in 'Ss':
        break

print(f'\nTotal da compra foi: {total:.2f}')

print(f'\nTemos {mais_que_mil} produtos custando mais de R$1000.00')

print(f'\nO produto mais barato foi {barato}, custando {menor:.2f}')

print(f'\nO produtor mais caro foi {caro}, custando {maior:.2f}')
