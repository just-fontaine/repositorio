numeros = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f'Os pares são: {sorted(numeros[0])}')

print(f'Os impares são: {sorted(numeros[1])}')
