print('')
salario = float(input('Salário: R$'))

sacima = salario + (salario * 10/100)
sabaixo = salario + (salario * 15/100)

print(' ')

if salario < 1250:
    print(f'\033[34mO novo salário é: R${sabaixo:.2f}\033[m')
else:
    print(f'\033[34mO novo salário é: R${sacima:.2f}\033[m')
