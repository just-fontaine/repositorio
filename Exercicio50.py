print('~~~~~CALCULANDO FATORIAL')
num = int(input('Digite o valor: '))
f = 1
c = num
print('')
while c > 0:
    f *= c
    c -= 1
print(f'O fatorial de {num} é {f}')

num = int(input('\nDigite o valor: '))
f = 1
c = num
for sequencia in range(num, 1, -1):
    f *= sequencia
    sequencia -= sequencia
print(f'\nO fatorial de {num} é {f}')
