vel = float(input('Qual a velocidade atual do carro: '))
velocidadeacima = vel - 80

print(' ')
if vel > 80:
    print(f'\033[31mVocê foi multado em R${velocidadeacima * 7:.2f}\033[m')
else:
    print('\033[34mVocê não está acima da velocidade.\033[m')
