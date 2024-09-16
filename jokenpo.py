import random
import time

print('\n\033[33mJogo: Pedra, Papel ou Tesoura!\033[m')

escolha_usuario = input('\nEscolha pedra, papel ou tesoura: ').lower()

if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
    print('\n\033[31mEscolha inválida. Escolha pedra, papel ou tesoura.')
    exit()

escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])

time.sleep(0.3)
print('JO')
time.sleep(0.3)
print('KEN')
time.sleep(0.3)
print('PO!!!')
time.sleep(0.3)

print(f'\nVocê escolheu \033[34m{escolha_usuario.capitalize()}\033[m e'
      f' o computador escolheu \033[31m{escolha_computador.capitalize()}\033[m.')

if escolha_computador == 'pedra' and escolha_usuario == 'pedra':
    print('\n\033[33mEmpate!\033[m')

elif escolha_usuario == 'papel' and escolha_computador == 'pedra':
    print('\n\033[34mVocê ganhou!\033[m')

elif escolha_usuario == 'tesoura' and escolha_computador == 'papel':
    print('\n\033[34mVocê ganhou!\033[m')

elif escolha_usuario == 'pedra' and escolha_computador == 'tesoura':
    print('\n\033[34mVocê ganhou!\033[m')

else:
    print('\n\033[31mVocê perdeu!\033[m')
