print('GERADOR DE PA')
print('-=-' * 10)

cont = 1
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
mais = 10
total = 0

print(termo, end=' > ')

while mais != 0:
    total += mais
    while cont <= total:
        termo += razao
        print(f'{termo} > ', end='')
        cont += 1
    print('PAUSA')
    mais = int(input('\nQUANTOS NÚMEROS A MAIS VOCÊ DESEJA MOSTRAR: '))
print('\nFIM')
print(f'\nPROGRESSÃO FINALIZADA. {total} NÚMEROS FORAM MOSTRADOS NO TOTAL.')
