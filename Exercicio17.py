frase = str(input('Digite a frase: ').strip())
frasem = frase.lower()
print(f'A letra "A" aparece {frasem.count('a')} vezes na frase)')

print(f'A primeira letra "A" aparece na posição: {frasem.find('a')+1}')

print(f'A ultima letra "A" aparece na posição: {frasem.rfind('a')+1}')
