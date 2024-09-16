nome = str(input('Qual o seu nome?: ').strip())

nomecortado = nome.split()
nomejunto = ''.join(nomecortado)
tamanho = len(nomejunto)

print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
print(f'Número de letras: {tamanho}')
print(f'Quantas letras tem o primeiro nome: {len(nomecortado[0])}')
