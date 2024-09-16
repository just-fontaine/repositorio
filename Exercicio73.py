exp = str(input('Digite sua expressão: '))
abrindo = fechando = 0
for letra in exp:
    if letra == '(':
        abrindo += 1
    if letra == ')':
        fechando += 1
if abrindo != fechando or exp[0] == ')':
    print('\n\033[31mA expressão esta errada.')
elif abrindo == fechando:
    print('\n\033[34mA expressão é válida.')
