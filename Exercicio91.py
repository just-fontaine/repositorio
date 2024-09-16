import datetime


def voto(ano_nascimento):
    idade_calculada = datetime.date.today().year - ano_nascimento
    if idade_calculada < 16:
        return 'Negado'
    elif 16 <= idade_calculada < 18 or idade_calculada >= 65:
        return 'Opcional'
    else:
        return 'Obrigatório'


nascimento = int(input('Ano do seu nascimento: '))
idade = datetime.date.today().year - nascimento

print(f'Você tem {idade} anos e seu voto em {datetime.date.today().year} é {voto(nascimento).lower()}')
