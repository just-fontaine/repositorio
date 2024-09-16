lado1 = float(input('Digite o lado 1: '))
lado2 = float(input('Digite o lado 2: '))
lado3 = float(input('Digite o lado 3: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('\n\033[34mÉ possível formar um triângulo.\033[m')
    if lado1 != lado2 != lado3 != lado1:
        print('\nO triângulo é \033[33mEscaleno\033[m.')
    if lado1 == lado2 == lado3:
        print('\nO triângulo é \033[33mEquilátero\033[m.')
    else:
        if lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
            print('\nO triângulo é \033[33mIsósceles\033[m.')
else:
    print('\n\033[31mNão é possível formar um triângulo.\033[m')
