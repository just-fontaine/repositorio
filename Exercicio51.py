print('\033[33m\n~~~~ 10 PRIMEIROS TERMOS DE UMA PROGRESSÃO ARITMÉTICA ~~~~\033[m')
termo = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + 9 * razao
print('')
print(termo, end=' > ')
while termo != decimo:
    termo += razao
    print(termo, end=' > ')
print('FIM')
