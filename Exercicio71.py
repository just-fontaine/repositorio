numeros = []

while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'Nn':
        break

numeros.sort(reverse=True)

print(f'\nVocê digitou {len(numeros)} valores.')

print(f'\nOs valores em ordem descrescente são: {numeros}')

if 5 in numeros:
    print('\nO número 5 faz parte da lista!')
else:
    print('\nO valor 5 não faz parte da lista!')
