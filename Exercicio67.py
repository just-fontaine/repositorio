palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:
    print(f'\n\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
print('')
