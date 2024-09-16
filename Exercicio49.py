import time
n1 = int(input('\nPrimeiro valor: '))
n2 = int(input('\nSegundo valor: '))
opcao = 0
while opcao != 5:
    time.sleep(1)
    print('\n[1] somar   [2] multiplicar   [3] maior   [4] novos números   [5]   sair do programa')
    opcao = int(input('\nQual a sua opção? '))
    if opcao == 1:
        print(f'\nA soma de {n1} + {n2} é {n1 + n2}.')
    if opcao == 2:
        print(f'\nO produto de {n1} e {n2} é {n1 * n2}.')
    if opcao == 3:
        if n1 == n2:
            print('\nOs números são iguais.')
        else:
            maior = n1
        if n2 > n1:
            maior = n2
            print(f'\nO maior valor é {maior}.')
    if opcao == 4:
        n1 = int(input('\nPrimeiro valor: '))
        n2 = int(input('\nSegundo valor: '))
    if opcao > 5:
        print('\nOpção inválida, escolha novamente.')

print('\nSaindo...')

time.sleep(2)
