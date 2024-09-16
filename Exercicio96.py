def escrever_bonitinho(texto):
    comprimento = len(texto) + 4
    print('~' * comprimento)
    print(f'{texto.center(comprimento)}')
    print('~' * comprimento)


escrever_bonitinho(f'SISTEMA DE AJUDA PYHELP')
print(f'"Fim" para parar')
print()
while True:
    ajuda = str(input('Função ou Biblioteca: '))
    if ajuda != 'fim':
        help(ajuda)
    if ajuda.lower().strip() in 'fim':
        break

print(f'FIM DO PROGRAMA')
