lado1 = float(input('Digite o lado 1: '))
lado2 = float(input('Digite o lado 2: '))
lado3 = float(input('Digite o lado 3: '))

if lado1 < lado2 + lado3 and lado3 < lado1 + lado2 and lado2 < lado1 + lado3:
    print('\n\033[34mÉ possível formar um triângulo.\033[m')
else:
    print('\n\033[31mNão é possível formar um triângulo.\033[m')
