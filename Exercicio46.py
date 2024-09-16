total = 0
mulher = 0
velhoidade = 0
velhonome = ''
for p in range(1, 5):
    print(f'---- {p}° PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    total += idade
    while sexo not in 'Ff' and sexo not in 'Mm':
        sexo = str(input('Sexo inválido. [Digite M/F]'))
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    if sexo in 'Mm' and p == 1:
        velhoidade = idade
        velhonome = nome
    if sexo in 'Mm' and idade > velhoidade:
        velhoidade = idade
        velhonome = nome
print(f'A média de idade do grupo é {total/4}.')
print(f'O homem mais velho tem {velhoidade} e se chama {velhonome}')
print(f'Ao todo são {mulher} mulher(es) com menos de 20 anos.')
