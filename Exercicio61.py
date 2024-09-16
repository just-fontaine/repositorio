# 50, 20, 10, 1

cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0

print('=' * 35)
print('        BANCO HIPOTÉTICO')
print('=' * 35)

while True:
    valor = int(input('Qual valor você quer sacar: R$'))
    while True:
        if valor >= 50:
            valor -= 50
            cedulas50 += 1
        else:
            break
    while True:
        if valor >= 20:
            valor -= 20
            cedulas20 += 1
        else:
            break
    while True:
        if valor >= 10:
            valor -= 10
            cedulas10 += 1
        else:
            break
    while True:
        if valor >= 1:
            valor -= 1
            cedulas1 += 1
        else:
            break
    break

print('=' * 35)

if cedulas50 != 0:
    print(f'{cedulas50} cédulas de R$50')
if cedulas20 != 0:
    print(f'{cedulas20} cédulas de R$20')
if cedulas10 != 0:
    print(f'{cedulas10} cédulas de R$10')
if cedulas1 != 0:
    print(f'{cedulas1} cédulas de R$1')
