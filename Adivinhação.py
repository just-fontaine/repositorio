import random
from time import sleep
print(' ')
print('               \033[33m~Jogo da adivinhação~\033[m')
print(' ')
print('Vou pensar num número de 1 a 3, tente adivinhar!')
n = random.randint(1, 3)  # Número do Computador
print(' ')

num = int(input('Em que número pensei? '))  # Número do Jogador
print(' ')
print('\033[33mPROCESSANDO...\033[m')

sleep(2)

print(' ')
if num == n:
    print('\033[34mVocê acertou!\033[m')
else:
    print(f'\033[31mVocê errou... Eu pensei no número {n}\033[m')
    print(' ')
    sleep(1)
    print('\033[31mTente novamente...\033[m')
