import datetime

# Pegar as informações
while True:
    nome = str(input('Nome: '))
    ano_nascimento = int(input('Ano de nascimento: '))
    carteira = str(input('Carteira de Trabalho (0 não tem): '))
    # Se não tiver carteira ele para
    if carteira[0] == '0':
        # Cálculo da idade (pegar o ano atual e subtrair o ano de nascimento)
        ano_atual = datetime.date.today().year

        # Criação do dicionário simples
        pessoa = {
            'Nome': nome,
            'Idade': ano_atual - ano_nascimento,
            'CTPS': carteira,
        }

        # Exibir dicionário
        print('-=' * 30)
        for k, v in pessoa.items():
            print(f'{k}: {v}')
        break

    ano_contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))

    # Cálculo da idade (pegar o ano atual e subtrair o ano de nascimento)
    hoje = datetime.date.today()
    ano_atual = hoje.year

    # Criação do dicionário simples
    pessoa = {
        'Nome': nome,
        'Idade': ano_atual - ano_nascimento,
        'CTPS': carteira,
        'Ano de contratação': ano_contratacao,
        'Salário': salario,
        'Aposentadoria': (ano_contratacao - ano_nascimento) + 35,
    }

    # Exibir dicionário
    print('-=' * 30)
    for k, v in pessoa.items():
        print(f'{k}: {v}')
    break
