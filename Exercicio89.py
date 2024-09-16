def maior(*num):
    if len(num) > 0:
        print(f'Números: {num}')
        print(f'O maior valor foi: ', end='')
        print(max(num))
        print()
    else:
        print('Nenhum valor foi informado')


print(f'Digite os números desejados (0 para parar)')
numeros = []
n = 1
while n != 0:
    n = int(input('Número: '))
    if n != 0:
        numeros.append(n)
numeros = tuple(numeros)
maior(*numeros)
