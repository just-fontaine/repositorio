import random

print('\033[33m[[[ JOGO DA ADIVINHAÇÃO v2.0 ]]]\033[m')
print('\033[33m\nVou pensar em um número de 0 a 10...\033[m')

escolha = 1
computador = random.randint(0, 10)
usuario = int(input('\nQual é seu palpite? '))

if usuario == computador:
    print('\n\033[34mVocê ganhou!')

while usuario != computador:
    if usuario > computador:
        usuario = int(input('\n\033[31mMenos... Tente novamente: '))
        escolha += 1
    if usuario < computador:
        usuario = int(input('\n\033[31mMais... Tente novamente: '))
        escolha += 1
    if usuario == computador:
        print(f'\n\033[34mVocê ganhou com {escolha} tentativas!')
