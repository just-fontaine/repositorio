def calcular_media(a, b):
    return (a + b) / 2


nome = str(input('Nome: '))
nota1 = float(input(f'Nota 1 de {nome}: '))
nota2 = float(input(f'Nota 2 de {nome}: '))
media = calcular_media(nota1, nota2)

if media <= 5:
    situacao = 'Reprovado'
elif media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'

aluno = {
    'Nome': nome,
    'Média': media,
    'Situação': situacao
}

print()

for k, v in aluno.items():
    print(f'{k}: {v}')
