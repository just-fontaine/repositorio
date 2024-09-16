from utilidadescev import moeda

valor = float(input('Preço: R$'))
aumento = float(input('Aumento (%): '))
reducao = float(input('Redução (%): '))

moeda.resumo(valor, aumento, reducao, m=True)
