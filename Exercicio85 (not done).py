def linha():
    print('-=' * 30)


# Declarar dicionário, lista e total
time = []
jogador = dict()
gols = []
# Pegar informações
while True:
    jogador.clear()
    tot = 0
    gols = []
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for p in range(partidas):
        partida = int(input(f'Quantos gols na partida {p + 1}: '))
        gols.append(partida)
        tot += partida
    jogador['Gols'] = gols[:]
    jogador['Total'] = tot
    time.append(jogador.copy())
    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continuar in 'Nn':
        break

# Mostrar informações
print(time)

'''if partidas == 0 or partidas == 1:
    print(f'O jogador {jogador["Nome"]} jogou {partidas} partida.')
else:
    print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c in range(partidas):
    print(f'Na partida {c + 1}, fez {gols[c]} gols.')
print(f'Total de {tot} gols.')'''
