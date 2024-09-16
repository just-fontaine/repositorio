frase = str(input('\nDigite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('\nÉ um palíndromo.')
else:
    print('\nNão é um palindromo.')

print(f'\nO inverso de {junto} é {inverso}.')
