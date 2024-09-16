numeros = []
maior = menor = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite o valor para a posição {n}: ')))
    if n == 0:
        maior = menor = numeros[0]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]

print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for n, v in enumerate(numeros):
    if v == maior:
        print(f'{n}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições: ', end='')

for n, v in enumerate(numeros):
    if v == menor:
        print(f'{n}...', end='')

print()
