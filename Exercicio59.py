mulhernova = total = homem = 0
while True:
    print('-=-' * 10)
    print('           CADASTRO')
    print('-=-' * 10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    while sexo not in 'MFmf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    if idade >= 18:
        total += 1
    if sexo in 'm':
        homem += 1
    if sexo in 'f' and idade < 20:
        mulhernova += 1
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    print('-=-' * 10)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if continuar in 'n':
        print('-=-' * 10)
        break
print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo são {homem} homens cadastrados.')
print(f'E temos {mulhernova} mulheres com menos de 20 anos.')
