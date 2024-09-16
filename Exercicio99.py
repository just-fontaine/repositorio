from utilidadescev import moeda

valor = float(input('Preço: R$'))
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.dobro(valor, True)}')
print(f'Metade de {moeda.moeda(valor)} é: {moeda.metade(valor, True)}')
print(f'{moeda.moeda(valor)} aumentado em 10%: {moeda.aumentar(valor, 10, True)}')
print(f'{moeda.moeda(valor)} reduzido em 13%: {moeda.reduzir(valor, 13, True)}')
