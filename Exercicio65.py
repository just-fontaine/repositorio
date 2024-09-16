numeros = (int(input('Digite um número: ')),
           int(input('Digite outro: ')),
           int(input('Digite mais um: ')),
           int(input('Digite o último número: ')))

print(f'\nVocê digitou os números {numeros}')

if numeros.count(9) == 0:
    print('O número 9 não apareceu nenhuma vez.')
elif numeros.count(9) > 1:
    print(f'O número 9 apareceu {numeros.count(9)} vezes.')
else:
    print(f'O número 9 apareceu {numeros.count(9)} vez.')

if 3 in numeros:
    print(f'O número 3 apareceu pela primeira vez na posição {numeros.index(3) + 1}')
else:
    print('O número 3 não apareceu nenhuma vez.')

print('Os números pares foram: ', end='')

for c in numeros:
    if c % 2 == 0 or c == 0:
        print(c, end=' ')
    else:
        break
