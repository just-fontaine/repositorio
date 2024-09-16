num = float(input('Digite um número inteiro: '))
print(' ')
if num % 2 == 0:
    print(f'O número é \033[34m{num}\033[m é par.')
else:
    print(f'O número é \033[31m{num}\033[m é impar.')
