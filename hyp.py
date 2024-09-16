import math

cat1 = float(input("Digite o valor do cateto 1: "))
cat2 = float(input("Digite o valor do cateto 2: "))
hyp = math.hypot(cat1, cat2)

print('ㅤㅤㅤㅤ| ⬊')
print('ㅤㅤㅤㅤ|  ⬊')
print(f'ㅤㅤㅤㅤ|   ⬊  \033[34m{hyp:.1f}\033[m ')
print(f' \033[31m{cat1}\033[mㅤ |    ⬊')
print('ㅤㅤㅤㅤ|     ⬊')
print('ㅤㅤㅤㅤ|      ⬊')
print('ㅤㅤㅤㅤ----------')
print(f'ㅤㅤㅤㅤㅤ ㅤ \033[31m{cat2}\033[m ')

print(f'\nA hipotenusa vale: \033[34m{hyp:.1f}\033[m')

