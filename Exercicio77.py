matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posição [{linha},{coluna}]: '))

print('MATRIZ 9x9: ')
print('-=' * 34)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'        [{matriz[linha][coluna]:^10}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()

print('-=' * 34)
print(f'A soma dos pares é: {spar}')

for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {scol}')

for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print(f'O maior valor da segunda linha é {maior}')
