def calcular_media(a, b):
    return (a + b) / 2


alunos = []
temp = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = calcular_media(nota1, nota2)

    temp.append(nome)
    temp.append(media)
    alunos.append(temp[:])
    temp.clear()

    continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if continuar in 'n':
        break

print(alunos)
