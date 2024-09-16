from datetime import date

atual = date.today().year
nasc = int(input('Ano do seu nascimento: '))
idade = atual - nasc
print(f'\nQuem nasceu em {nasc} vai fazer {idade} anos em {atual}.')

if idade == 18:
    print('\nVocê precisa se alistar esse ano.')
elif idade < 18:
    print(f'\nVocê vai se alistar daqui {18 - idade} ano(s).')
else:
    print(f'\nVocê deveria ter se alistado há {idade - 18} ano(s).')
