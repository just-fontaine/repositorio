num = int(input('Digite um número: '))
tot = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='\033[m ')
if tot != 2:
    print('\n\nNão é primo.')
else:
    print('\n\nÉ primo')
