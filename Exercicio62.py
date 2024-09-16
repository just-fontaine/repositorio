numeros = tuple(('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
                 'dezessete', 'dezoito', 'dezenove', 'vinte'))
while True:
    num = int(input('Digite um número de 0 a 20: '))
    while num < 0 or num > 20:
        if num < 0:
            num = int(input('\033[31m\nNúmero muito pequeno. Tente novamente:\033[m '))
        if num > 20:
            num = int(input('\033[31m\nNúmero muito grande. Tente novamente: \033[m'))

    print(f'Você digitou o número: \033[32m{numeros[num]}\033[m')

    continuar = str(input('\nVocê quer continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'n':
        break
    while continuar not in 'sn':
        continuar = str(input('Você quer continuar? [S/N] ')).lower().strip()[0]

print('\nFIM DO PROGRAMA.')
