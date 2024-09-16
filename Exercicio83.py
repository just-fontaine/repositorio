def linha():
    print('-=' * 30)


# Declarar dicionário, lista e total
jogador = dict()
gols = []
tot = 0
# Pegar informações
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for p in range(partidas):
    partida = int(input(f'Quantos gols na partida {p + 1}: '))
    gols.append(partida)
    tot += partida
jogador['Gols'] = gols
jogador['Total'] = tot
linha()
# Mostrar informações (jeito 1)
print(jogador)
linha()
# Mostrar informações (jeito 2)
for k, v in jogador.items():
    print(f'{k}: {v}')
linha()
# Mostrar informações (jeito 3)
if partidas == 0 or partidas == 1:
    print(f'O jogador {jogador["Nome"]} jogou {partidas} partida.')
else:
    print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(partidas):
    print(f'Na partida {c + 1}, fez {gols[c]} gols.')
print(f'Total de {tot} gols.')
