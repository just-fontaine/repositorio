resp = 's'
soma = 0
cont = 0
maior = -9999999999999999999999999999999999999999999999999
menor = 99999999999999999999999999999999999999999999999999
while resp in 'Ss':
    num = int(input('Digite um número: '))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    soma += num
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
print(f'A média dos {cont} números foi de {soma / cont}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')
print('ACABOU')
