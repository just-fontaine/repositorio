import random

numeros = (random.randint(1, 20), random.randint(1, 20),
           random.randint(1, 20), random.randint(1, 20), random.randint(1, 20))


print('Os valores sorteados foram: ', end='')
for i, valor in enumerate(numeros):
    if i < len(numeros) - 1:
        print(valor, end=', ')
    else:
        print(valor)
