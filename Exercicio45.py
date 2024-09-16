menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O maior peso foi {maior}kg')
print(f'O menor peso foi {menor}kg')
