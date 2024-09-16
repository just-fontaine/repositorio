from utilidadescev import moeda

valor = float(input('Preço: R$'))
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.moeda(moeda.dobro(valor))}')
print(f'Metade de {moeda.moeda(valor)} é: {moeda.moeda(moeda.metade(valor))}')
print(f'{moeda.moeda(valor)} aumentado em 10%: {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'{moeda.moeda(valor)} reduzido em 13%: {moeda.moeda(moeda.reduzir(valor, 13))}')
