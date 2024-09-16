print('\n10 primeiros termos de uma \033[31m~Progressão Aritmética~\033[m')

termo = int(input('\nDigite o primeiro termo: '))
razao = int(input('\nDigite a razão: '))
decimo = termo + (11-1) * razao
for c in range(termo, decimo, razao):
    print(c, end=' > ')
print('ACABOU.')
