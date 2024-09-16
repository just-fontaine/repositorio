tabela = tuple(('Flamengo', 'Botafogo', 'Palmeiras', 'São Paulo', 'Bahia', 'Athletico-PR',
                'Cruzeiro', 'Fortaleza', 'Bragantino', 'Internacional', 'Juventude', 'Atlético-MG',
                'Vasco da Gama', 'Criciúma', 'EC Vitória', 'Cuiabá', 'Corinthians', 'Grêmio',
                'Atlético-GO', 'Fluminense'))

time = str(input('\nQual time você deseja procurar na tabela: ')).strip()

while time not in tabela:
    print('\nTime não encontrado, tente novamente. ')
    time = str(input('\nQual time você deseja procurar na tabela: ')).strip()

print(f'\nLista de times do Brasileirão: {tabela}')
print('-=-' * 100)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('-=-' * 100)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-=-' * 100)
print(f'O {time} se encontra na {tabela.index(time) + 1}° posição.')
print('-=-' * 100)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=-' * 100)
