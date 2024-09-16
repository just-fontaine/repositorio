# tabuada com for

valor = int(input('Limite da tabuada: '))
num = int(input('\n     Número: '))

print('')

for c in range(1, valor + 1):
    print(f'     {num} x {c} = {num * c}')
