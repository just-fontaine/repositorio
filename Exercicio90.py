import random


def sort_5_numeros():
    """
    ~SORTEIA 5 NÚMEROS~
    :return: retorna uma lista com 5 números aleatórios
    """
    numeros = []
    for n in range(0, 5):
        n = random.randint(1, 9)
        numeros.append(n)
    return numeros


def soma_dos_pares(*num):
    """
    ~SOMA TODOS OS NÚMEROS PARES DE UMA LISTA~
    :parâmetro num: lista de números
    :return: soma dos pares
    """
    somapar = 0
    for n in num:
        if n % 2 == 0:
            somapar += n
    return somapar


print('~' * 25)
for c in range(1, 5):
    numeros_sorteados = sort_5_numeros()
    print(f'Números sorteados: {numeros_sorteados}')
    print(f'Soma dos pares: {soma_dos_pares(*numeros_sorteados)}')
    print('~' * 25)
