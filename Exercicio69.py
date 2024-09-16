lista = []
print()

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso.')
    else:
        print('Numero repetido, não irei adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Digite apenas "S" ou "N": '))
    if continuar in 'Nn':
        break

lista.sort()
print(f'\nVocê digitou os valores: {lista}')
