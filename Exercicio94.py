def leiaint(msg):
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            numero = int(numero)
        else:
            print('\033[31mErro! digite um número inteiro válido.\033[m')
        if isinstance(numero, int):
            break
    return numero


# Programa principal
n = leiaint('Digite um número: ')
print(f'\nVocê digitou o número: {n}')
