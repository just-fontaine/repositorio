import random
import time

listacompleta = []
temp = []

print('-' * 40)
print('       JOGO DA MEGA SENA')
print('-' * 40)
print()

qj = int(input('Quantos jogos serão sorteados?: '))

if qj == 1:
    print(f'\n~~~~SORTEANDO {qj} JOGO~~~~')
else:
    print(f'\n~~~~SORTEANDO {qj} JOGOS~~~~')
print()

for quantidade in range(0, qj):
    for n in range(0, 6):
        num = random.randint(1, 61)
        while num in temp:
            num = random.randint(1, 61)
        temp.append(num)
    listacompleta.append(temp[:])
    temp.clear()


for jogos in range(0, qj):
    print(f'Jogo {jogos + 1}: {sorted(listacompleta[jogos])}')
    time.sleep(1)

print()
print('-=' * 5, end='')
print(' < BOA SORTE > ', end='')
print('-=' * 5)
