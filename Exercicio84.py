# Definir listas e dicionários
pessoa = {}
pessoas = []
mulheres = []
total_idade = 0
# Entrada de dados
while True:
    print('-=' * 30)
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    if pessoa['Sexo'][0] == 'F':
        mulheres.append(pessoa['Nome'])
    while pessoa['Sexo'] not in 'MF':
        print(f'ERRO! Digite apenas "M" ou "F"')
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()
        if pessoa['Sexo'][0].upper() == 'F':
            mulheres.append(pessoa['Nome'])
    pessoa['Idade'] = int(input('Idade: '))
    total_idade += pessoa['Idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip()
    print('-=' * 30)
    if continuar in 'Nn':
        break
    while continuar not in 'SsNn':
        print(f'ERRO! Digite apenas "S" ou "N"')
        continar = str(input('Quer continuar? [S/N]: ')).strip()

media = total_idade / len(pessoas)
# Exibição do total de pessoas
if len(pessoas) == 1:
    print(f'Ao todo temos {len(pessoas)} pessoa cadastradas.')
else:
    print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
print()
# Exibição da média de idade
print(f'A média de idade é: {media:.1f}')
print()
# Exibição do Total de mulheres cadastradas
if len(mulheres) == 0:
    print(f'Nenhuma mulher foi cadastrada.')
else:
    print(f'As mulheres cadastradas foram ', end='')
for m in mulheres:
    print(m, end=' ')
print()
# Exibição das pessoas com idade acima da média
print('Lista de pessoas com idade acima (ou igual) a média: ')
contador = 0
for p in pessoas:
    for k, v in p.items():
        if p['Idade'] >= media:
            if contador % 3 == 0:
                print('    ', end='')
            contador += 1
            print(f'{k}: {v};', end=' ')
            if contador % 3 == 0:
                print()
print('-=' * 30)
