import datetime

pessoa = dict()

pessoa['Nome'] = str(input('Nome: ')).capitalize()
nascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.date.today().year - nascimento
pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
while pessoa['Sexo'][0] not in 'MmFf':
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    if pessoa['Sexo'] == 'F':
        pessoa['Aposentadoria'] = pessoa['Ano de Contratação'] - nascimento + 30
    else:
        pessoa['Aposentadoria'] = pessoa['Ano de Contratação'] - nascimento + 35

for k, v in pessoa.items():
    if k == 'Salário':
        print(f'{k}: {v:.2f}')
    else:
        print(f'{k}: {v}')
