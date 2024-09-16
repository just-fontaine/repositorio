pessoas = []
maiores_pesos = []
menores_pesos = []
menor = maior = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    if len(maiores_pesos) == 0:
        maiores_pesos.append(nome)
        maior = peso
        menores_pesos.append(nome)
        menor = peso
    else:
        if peso == maior:
            maiores_pesos.append(nome)
        if peso > maior:
            while len(maiores_pesos) > 0:
                maiores_pesos.pop()
            maiores_pesos.append(nome)
            maior = peso
        if peso == menor:
            menores_pesos.append(nome)
        if peso < menor:
            while len(menores_pesos) > 0:
                menores_pesos.pop()
            menores_pesos.append(nome)
            menor = peso
    pessoas.append(nome)
    continuar = str(input('Quer continuar [S/N]: '))
    while continuar[0] not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]: '))
    if continuar[0] in 'Nn':
        break

print(f'\nVocê cadastrou {len(pessoas)} pessoas.')
print(f'\nO maior peso foi de {maior}kg. Peso de: ', end='')
for c, nome in enumerate(maiores_pesos):
    if c < len(maiores_pesos) - 1:
        print(nome, end=', ')
    else:
        print(nome, end='')

print(f'\nO menor peso foi de {menor}kg. Peso de: ', end='')
for c, nome in enumerate(menores_pesos):
    if c != len(menores_pesos) - 1:
        print(nome, end=', ')
    else:
        print(nome, end=' ')
