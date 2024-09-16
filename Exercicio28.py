print('\n~~~~Conversor~~~~')

n = int(input('\nDigite o valor: '))

conversao = str((input('\nEscolha a conversão (\033[31mhex, oct, bin\033[m): ').lower().strip()))

if conversao == 'bin' in conversao:
    print(f'\nO valor em binário é: \033[31m{bin(n)[2:]}\033[m')
elif conversao == 'oct' in conversao:
    print(f'\nO valor em octal é \033[31m{oct(n)[2:]}\033[m')
elif conversao == 'hex' in conversao:
    print(f'\nO valor em hexadecimal é: \033[31m{hex(n)[2:]}\033[m')
else:
    print('\n\033[31mDigite uma das conversões possíveis.\033[m')
