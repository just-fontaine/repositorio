sexo = str(input('Informe seu sexo [M/F]: ')).lower().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).lower().strip()[0]
if sexo == 'm':
    sexo = 'Masculino'
if sexo == 'f':
    sexo = 'Feminino'

print(f'\nSexo {sexo} registrado com sucesso!')
