import random
import time
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
while True:
    time.sleep(1)
    print('-=' * 30)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] randomizar números (0 a 100)')
    print('[5] novos números')
    print('[6] sair do programa')
    print('-=' * 30)
    opcao = str(input('Opção: '))
    while opcao not in '123456' or opcao == '':
        opcao = str(input('Opção: '))
    if opcao in '1':
        print(f'{num1}+{num2}={num1 + num2}')
    if opcao in '2':
        print(f'{num1}x{num2}={num1 * num2}')
    if opcao in '3':
        print(f'O maior valor é {max(num1, num2)}')
    if opcao in '4':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Os números randomizados foram {num1} e {num2}')
    if opcao in '5':
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))
    if opcao in '6':
        break
print('Saindo...')
time.sleep(1)
print('\nFIM DO PROGRAMA')
