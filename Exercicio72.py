lista = []
listaimpares = []
listapares = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapares.append(num)
    else:
        listaimpares.append(num)
    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'Nn':
        break

print(f'\nA lista inteira é: {lista}')
print(f'\nA lista dos pares é {listapares}')
print(f'\nA lista dos impares é {listaimpares}')
