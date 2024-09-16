num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))

if num1 > num2:
    print(f'\nO número \033[34m{num1}\033[m é maior.')
elif num2 > num1:
    print(f'\nO número \033[34m{num2}\033[m é maior')
else:
    print('\n\033[33mNenhum número é maior.\033[m')
