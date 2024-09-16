from utilidadescev import moeda

valor = float(input('Preço: R$'))
print(f'O dobro de {valor:.2f} é: {moeda.dobro(valor):.2f}')
print(f'Metade de {valor:.2f} é: {moeda.metade(valor):.2f}')
print(f'{valor:.2f} aumentado em 10%: {moeda.aumentar(valor, 10):.2f}')
print(f'{valor:.2f} reduzido em 13%: {moeda.reduzir(valor, 13):.2f}')
