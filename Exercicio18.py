nome = str(input('Qual o seu nome completo? ').strip())

nomelista = nome.split()

print(f'Seu primeiro nome é: \033[31m{nomelista[0].capitalize()}\033[m')
print(f'Seu ultimo nome é: \033[34m{nomelista[len(nomelista)-1].capitalize()}\033[m')
