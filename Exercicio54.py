num = 0
total = 0
resultado = 0
while num != 999:
    num = int(input('\nDigite um número [999 para parar]: '))
    if num != 999:
        total += 1
        resultado = resultado + num
    if num == 999:
        print(f'\nA soma dos {total} números foi {resultado}.')
