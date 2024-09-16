def mensagem(n='<desconhecido>', g=0):
    if g == 1:
        print(f'O jogador {n} fez {g} gol no campeonato.')
    else:
        print(f'O jogador {n} fez {g} gols no campeonato.')


nome = input('Nome do jogador: ').strip()
gols = input('Número de gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    mensagem(g=gols)
else:
    mensagem(nome, gols)
