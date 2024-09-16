import time
print('Subtração de números reais.')
time.sleep(1)
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
s = n1 - n2
print(f'A subtração entre '
      f'\033[34m{n1}\033[m e '
      f'\033[34m{n2}\033[m vale '
      f'\033[31m{s}\033[m')
