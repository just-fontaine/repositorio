def fatorial(n=1, show=False):
    """
    ~CALCULA O FATORIAL DE 'n'~
    :param n: número a ser calculado
    :param show: mostrar o cálculo na tela (bool)
    Se o parâmetro 'show' for Falso:
        :return: retorna apenas o resultado
    Caso o parâmetro 'show' for Verdadeiro:
        :return: retorna o resultado e as multiplicações
    """

    resultado = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        resultado *= c
    if show:
        print(resultado)
        return None
    else:
        return resultado


print('~' * 30)
print('Cálculo de fatorial')
print('~' * 30)

numero = int(input('Número: '))
mostrar = str(input('Mostrar o Cálculo? [S/N]: ')).strip().upper()

if mostrar == 'S':
    mostrar = True
else:
    mostrar = False

r = fatorial(numero, show=mostrar)
if not mostrar:
    print(f'\n{r}')
