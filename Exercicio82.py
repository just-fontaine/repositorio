import datetime

# Pegar as informações
while True:
    nome = str(input('Nome: '))
    ano_nascimento = int(input('Ano de nascimento: '))
    carteira = str(input('Carteira de Trabalho (0 não tem): '))
    # Se não tiver carteira ele para
    if carteira[0] in '0':
        break
    ano_contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    break

# Cálculo da idade (pegar o ano atual e subtrair o ano de nascimento)
hoje = datetime.date.today()
ano_atual = hoje.year

# Criação do dicionário simples
pessoa = {
    'Nome': nome,
    'Idade': ano_atual - ano_nascimento,
    'CTPS': carteira,
}

# Adicionar mais valores caso carteira de trabalho for existente
if carteira != '0':
    pessoa['Ano de contratação'] = ano_contratacao
    aposentadoria = (pessoa['Ano de contratação']) - ano_nascimento + 35
    pessoa['Salário'] = salario
    pessoa['Aposentadoria'] = aposentadoria


# Exibir dicionário
print('-=' * 30)
for k, v in pessoa.items():
    if k == 'Salário':
        print(f'{k}: {v:.2f}')
    else:
        print(f'{k}: {v}')
