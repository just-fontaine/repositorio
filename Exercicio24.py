num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

print(f'Maior número: \033[34m{max(num1, num2, num3):.1f}\033[m')
print(f'Menor número: \033[31m{min(num1, num2, num3):.1f}\033[m')
