import time
n = input('Digite algo: ')
time.sleep(0.5)
if n.isnumeric():
    print(f'Isso é número?: \033[34m{n.isnumeric()}\033[m')
else:
    print(f'Isso é número?: \033[31m{n.isnumeric()}\033[m')
time.sleep(0.5)
if n.isspace():
    print(f'Tem apenas espaços?: \033[34m{n.isspace()}\033[m')
else:
    print(f'Tem apenas espaços?: \033[31m{n.isspace()}\033[m')

time.sleep(0.5)

if n.isalpha():
    print(f'É alfabético?: \033[34m{n.isalpha()}\033[m')
else:
    print(f'É alfabético?: \033[31m{n.isalpha()}\033[m')

time.sleep(0.5)

if n.isalnum():
    print(f'É alfanúmerico?: \033[34m{n.isalnum()}\033[m')
else:
    print(f'É alfanúmerico?: \033[31m{n.isalnum()}\033[m')

time.sleep(0.5)

if n.isascii():
    print(f'É ascii? \033[34m{n.isascii()}\033[m')
else:
    print(f'É ascii? \033[31m{n.isascii()}\033[m')

time.sleep(0.5)

if n.istitle():
    print(f'Está capitalizada?: \033[34m{n.istitle()}\033[m')
else:
    print(f'Está capitalizada?: \033[31m{n.istitle()}\033[m')
