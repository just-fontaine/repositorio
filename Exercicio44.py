maior = 0
menor = 0

print('')

for c in range(1, 8):
    data = int(input(f'Em que ano a pessoa {c} nasceu: '))
    idade = 2024 - data

    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'\nTivemos {maior} pessoas maiores de idade')

print(f'\nTivemos {menor} pessoas menores de idade')
