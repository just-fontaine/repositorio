matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posição [{linha},{coluna}]: '))

print('MATRIZ 9x9: ')
print('-=' * 34)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'        [{matriz[linha][coluna]:^10}]', end='')
    print()
print('-=' * 34)
