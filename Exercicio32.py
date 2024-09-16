import datetime

nasc = int(input('Digite o seu ano de nascimento: '))

atual = datetime.date.today().year

idade = atual - nasc

if idade < 9:
    print(f'\nSua idade é \033[31m{idade}\033[m e sua categoria é: MIRIM')

elif idade < 14:
    print(f'\nSua idade é \033[31m{idade}\033[m e sua categoria: INFANTIL')

elif idade < 19:
    print(f'\nSua idade é \033[31m{idade}\033[m e sua categoria: JUNIOR')

elif idade < 25:
    print(f'\nSua idade é \033[31m{idade}\033[m e sua categoria: SÊNIOR')

else:
    print(f'\nSua idade é \033[31m{idade}\033[m e sua categoria: MASTER')
