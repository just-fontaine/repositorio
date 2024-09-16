import random

print('-=-' * 20)
print('JOGO PAR OU IMPAR')
print('-=-' * 20)

vitorias = 0

while True:
    usuario = int(input('\nDiga um número: '))
    escolha = str(input('Par ou Impar? [P/I]: ')).lower().strip()[0]
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Impar? [P/I]: ')).lower().strip()[0]
    computador = random.randint(1, 2)
    soma = usuario + computador
    if soma % 2 == 0:
        par_ou_impar = 'PAR'
    else:
        par_ou_impar = 'IMPAR'
    if soma % 2 == 0 and escolha in 'p':
        print('\n\033[34mVocê venceu!\033[m')
        print(f'\nVocê jogou \033[33m{usuario}\033[m e o computador '
              f'\033[33m{computador}\033[m e o resultado foi \033[33m{soma}\033[m.\n\nDEU {par_ou_impar}!')
        vitorias += 1
    elif soma % 2 != 0 and escolha in 'i':
        print(f'\nVocê jogou \033[33m{usuario}\033[m e o computador '
              f'\033[33m{computador}\033[m e o resultado foi \033[33m{soma}\033[m.\n\nDEU {par_ou_impar}!')
        print('\n\033[34mVocê venceu!\033[m')
        vitorias += 1
    else:
        print(f'\nVocê jogou \033[33m{usuario}\033[m e o computador '
              f'\033[33m{computador}\033[m e o resultado foi \033[33m{soma}\033[m.\n\nDEU {par_ou_impar}!')
        print('\n\033[31mVocê perdeu!\033[m')
        break
print(f'\nGAME OVER! Você venceu \033[33m{vitorias}\033[m vez(es).')
