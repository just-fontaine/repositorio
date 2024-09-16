import datetime
ano = int(input('Digite o ano! (Para analisar o ano atual digite 0) ',))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\nO ano de \033[34m{ano}\033[m é um ano bissexto.')
else:
    print(f'\nO ano de \033[31m{ano}\033[m não é um ano bissexto')
