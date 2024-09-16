import math
real = float(input("Digite um valor em real: "))
print(f'\033[35mA parte inteira de {real} é {int(real)}\033[m')

print(f'\033[31mA parte inteira de {real} é {math.trunc(real)}\033[m\033[m')

print(f'\033[34mA parte inteira de {real} é {real:.0f}\033[m')
