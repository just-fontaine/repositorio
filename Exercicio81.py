import random
import time

jogadores = {
    'Jogador1': random.randint(1, 6),
    'Jogador2': random.randint(1, 6),
    'Jogador3': random.randint(1, 6),
    'Jogador4': random.randint(1, 6)
}

print('\nValores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    time.sleep(1)

jogadores_ordenados = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

print('\nRanking dos jogadores:')
for c, (k, v) in enumerate(jogadores_ordenados.items()):
    print(f'{c + 1}° Lugar: {k} com {v}')
    time.sleep(1)
