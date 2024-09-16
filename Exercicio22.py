distancia = float(input('Digite a distancia em km: '))

dabaixo = distancia * 0.50
dacima = distancia * 0.45
print(' ')
if distancia < 200:
    print(f'\033[34mO preço da viagem é R${dabaixo:.2f}\033[m')
else:
    print(f'\033[34mO preço da viagem é R${dacima:.2f}\033[m')
